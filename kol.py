import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8210866851:AAHRkDyIxPEfr_ALiQhkmrQjat9HP8z0Jmo"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🎡 Играть",
                web_app=WebAppInfo(url="http://127.0.0.1:5000")  # локально для теста
            )]
        ]
    )
    await message.answer("Привет! Нажми кнопку, чтобы открыть колесо фортуны:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())