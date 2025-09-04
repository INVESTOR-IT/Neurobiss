from fastapi import APIRouter, Request
from loguru import logger
from dotenv import load_dotenv

import aiogram
import os

from app.servise.servise import parse_amocrm_webhook_data
from app.ai.ai import text_processing_using_openai

load_dotenv()

router = APIRouter()
BOT = aiogram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
CHAT_ID = os.getenv('CHAT_ID')


@router.get('/health')
async def health():
    return {"status": "ok", "service": "amo_test", "version": "1.0.0"}


@router.post('/amocrm_webhook', status_code=200)
async def amocrm_webhook(request: Request):
    form_data = await request.form()
    result = await parse_amocrm_webhook_data(form_data)
    # result_openai = await text_processing_using_openai(result)
    await BOT.send_message(chat_id=CHAT_ID, text=result)  # text=result_openai
    logger.info(f'Данные отправлены пользователю: {CHAT_ID}')
