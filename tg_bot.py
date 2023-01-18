from aiogram import Bot, executor, Dispatcher, types
from sqlite_lib import db_start, user_connect

token = '5839626263:AAH6mCa4c72LBzF5Lj9DiRX7az3AT7SMZqs'

bot = Bot(token=token)
disp = Dispatcher(bot=bot)


async def on_startup(_):
    await db_start()


@disp.message_handler()
async def record_data(msg: types.Message) -> None:
    # print(msg)
    await user_connect(msg)
    await msg.answer(msg.text)  # ECHO


if __name__ == '__main__':
    executor.start_polling(disp, on_startup=on_startup)
