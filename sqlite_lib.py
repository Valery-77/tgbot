import sqlite3 as sql
import datetime

db_name = 'tgbot_db.db'
table_name = 'bot_userdata'


async def db_start():
    db = sql.connect(db_name)
    crs = db.cursor()
    crs.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (registration datetime, channel TEXT, id INTEGER PRIMARY 
    KEY, username TEXT, first_name TEXT, last_name TEXT, email TEXT, mobile TEXT, link TEXT, utm_source TEXT, 
    utm_campaign TEXT, utm_medium TEXT, utm_term TEXT, utm_content TEXT, last_visit datetime)""")
    db.commit()
    crs.close()


async def user_connect(msg):
    db = sql.connect(db_name)
    crs = db.cursor()
    user_id = msg.from_user.id
    cur_date = datetime.date.today()
    user = crs.execute(f"SELECT 1 FROM {table_name} WHERE id == {user_id}").fetchone()
    if not user:
        fst_name = msg.from_user.first_name
        lst_name = msg.from_user.last_name
        user_name = msg.from_user.username
        crs.execute(f"INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (cur_date, '', user_id, user_name, fst_name, lst_name, '', '', '', '', '', '', '', '', cur_date))
    else:
        crs.execute(f"UPDATE {table_name} SET last_visit = {cur_date} WHERE id == {user_id}")
    db.commit()
    crs.close()
