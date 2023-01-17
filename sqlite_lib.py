import sqlite3 as sql
import datetime

db_name = 'tgbot_db.db'
table_name = 'bot_userdata'


async def db_start():
    global db, crs

    db = sql.connect(db_name)
    crs = db.cursor()

    crs.execute(f"""CREATE TABLE IF NOT EXIST {table_name} (registration TEXT, channel TEXT, id INTEGER PRIMARY KEY, 
    username TEXT, first_nameTEXT, last_name TEXT, email TEXT, mobile TEXT,	link TEXT, utm_source TEXT,
    utm_campaign TEXT, utm_medium TEXT, utm_term TEXT, utm_content TEXT, last_visit TEXT)""")

    db.commit()
    crs.close()


async def user_connect(user_id):
    user = crs.execute("SELECT 1 FROM 'tb_name' WHERE id == 'key'".
                       format(tb_name=table_name, key=user_id)).fetchone()
    cur_date = datetime.date.today()
    if not user:
        crs.execute(f"INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (cur_date, '', user_id, '', '', '', '', '', '', '', '', '', '', '', cur_date))
        db.commit()
    else:
        crs.execute(f"UPDATE {table_name} SET last_visit = {cur_date} WHERE id == {user_id}")
        db.commit()
