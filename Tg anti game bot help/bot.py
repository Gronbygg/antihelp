from aiogram import Bot, Dispatcher, F, types, filters, handlers, Router
from aiogram.filters import Command, CommandObject, CommandStart, Filter, MagicData
import aiogram.utils.markdown as fmt
import asyncio
from aiogram.types import ContentType

token="7800281697:AAEjbqYZp5PJN3vDO7yfnmr99DVTZXrPZXk"

bot = Bot(token="7800281697:AAEjbqYZp5PJN3vDO7yfnmr99DVTZXrPZXk")
dp = Dispatcher(bot=bot)

@dp.message(Command("start")) 
async def cmd_start(msg: types.Message) -> None:
    hello_msg = await msg.answer("Привіт! Цей бот просто показує правила цієї группи якщо прописати !правила групи")
    await asyncio.sleep(30)
    await bot.delete_message(chat_id=hello_msg.chat.id, message_id=hello_msg.message_id)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)

@dp.message(F.text == "правила групи")
@dp.message(F.text == "!правила групи") 
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('<b>Натиснувши на написи ви можете побачити відповідну інформацію</b>\n\n'
                     
'<a href="https://telegra.ph/Pravila-chatu-10-20-2"><b>Правила чату</b></a>\n\n'

'<a href="https://telegra.ph/Pravila-gri-10-20-2"><b>Правила гри</b></a>\n\n'

'<a href="https://telegra.ph/probna-vers%D1%96ya-10-20"><b>Всі інші правила та інформація про чат</b></a>\n\n', parse_mode="HTML", disable_web_page_preview=True
)






#@dp.message()
#async def filter_message(message: types.Message):
#    if "http://telegra.ph/rules-06-18-5" in message.text:
#        await message.delete()
#        if "https://telegra.ph/rules-06-18-5" in message.text:
#           await message.delete()
#    else: 
#       await message.delete()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
