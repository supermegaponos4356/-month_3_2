
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message




BOT_TOKEN = "8676678514:AAEiR43jrIU8crVg7UcXC5yGqaREsftoH1U"



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()




@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"привет, {message.from_user.full_name} я твой бот"




    ) 






@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        "/start - приветствие\n"
        "/help - список команд"
    )
    print(f"пользователь {message.from_user.full_name} написал старт")










@dp.message()
async def echo(message: Message):
    await message.answer(f"ты написал {message.text}")






async def main():
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


























