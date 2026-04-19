import asyncio
import json
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

BOT_TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"
GAME_URL = "https://твой-username.github.io/repo/index.html"  # замени на свой хостинг

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=" Играть в Doodle Jump", web_app=WebAppInfo(url=GAME_URL))]
        ]
    )
    await message.answer(
        " *Doodle Jump в Telegram Mini App*\n\n"
        " Управление:\n"
        "• Стрелки ← → на ПК\n"
        "• Нажми на левую/правую часть экрана на телефоне\n"
        "• Наклон телефона (гироскоп)\n\n"
        "После проигрыша нажми /start заново, чтобы перезапустить игру.",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Нажми /start → кнопка 'Играть'. Прыгай по платформам, не упади!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())