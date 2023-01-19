from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import AllowedUpdates

from sqlite_lib import db_start, user_connect
from aiogram.utils.deep_linking import get_start_link, decode_payload, get_startgroup_link
from utm import get_utm

token = '5839626263:AAH6mCa4c72LBzF5Lj9DiRX7az3AT7SMZqs'

bot = Bot(token=token)
disp = Dispatcher(bot=bot, storage=MemoryStorage())


async def on_startup(_):
    await db_start()


@disp.message_handler(commands=['link'])
async def get_link(msg: types.Message):
    pass
    # lnk = """utm_source=tst_source&utm_medium=tst_medium&utm_campaign=tst_compaign&utm_content=tst_content&utm_term
    # =tst_term"""
    # link = await get_startgroup_link(lnk, encode=False)
    # print(link)
    # print(msg.get_args())
    # await user_connect(msg)
    # await msg.answer(link)  # ECHO


@disp.message_handler()
async def record_data(msg: types.Message):
    print(msg.text)
    await user_connect(msg)
    await msg.answer(msg.text)  # ECHO


if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True, allowed_updates=AllowedUpdates.all(), on_startup=on_startup)
