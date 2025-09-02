from fastapi import APIRouter, Request

from app.servise.servise import parse_amocrm_webhook_data


router = APIRouter()


@router.get('/health')
async def health():
    return {"status": "ok", "service": "amo_test", "version": "1.0.0"}


@router.post('/amocrm_webhook')
async def amocrm_webhook(request: Request):
    form_data = await request.form()
    result = await parse_amocrm_webhook_data(form_data)
