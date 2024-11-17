from aiogram import Bot, Dispatcher, F, types, filters, handlers, Router
from aiogram.filters import Command, CommandObject, CommandStart, Filter, MagicData
import asyncio

token="7715944881:AAHZHq1vnTrPm9o_igGbtWVbxSAt48376vg"

bot = Bot(token="7715944881:AAHZHq1vnTrPm9o_igGbtWVbxSAt48376vg")
dp = Dispatcher(bot=bot)

@dp.message(Command("start")) 
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("Привіт! Цей бот нічого з себе не представляє він всього лише видаляє правила Gamebot котрі можуть призиватися після команди !правила.")


@dp.message()
async def filter_message(message: types.Message):
    if "http://telegra.ph/rules-06-18-5" in message.text:
        await message.delete()
        if "https://telegra.ph/rules-06-18-5" in message.text:
           await message.delete()
    else: 
       await message.delete()
    





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
