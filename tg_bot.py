from aiogram import Bot, executor, Dispatcher, types
from sqlite_lib import db_start as start
token = '5839626263:AAH6mCa4c72LBzF5Lj9DiRX7az3AT7SMZqs'

bot = Bot(token=token)
disp = Dispatcher(bot=bot)

@disp.message_handler()
async def send_echo(msg: types.Message) -> None:
    print(msg)
    await msg.answer(msg.text)


if __name__ == '__main__':
    start()
    executor.start_polling(disp)
