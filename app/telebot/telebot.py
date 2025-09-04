# Данный скрипт нужен для получения CHAT_ID

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from loguru import logger

import asyncio
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    '''
    Выводит chat_id пользователя, который начал диалог с ботом.
    '''

    chat_id = message.chat.id
    logger.info(f'Chat_id пользователя: {chat_id}')
    await message.reply('Привет! Я тебя запомнил!')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
