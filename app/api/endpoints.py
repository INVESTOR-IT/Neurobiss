from fastapi import APIRouter


router = APIRouter()


@router.get('/health')
async def health():
    return {"status": "ok", "service": "amo_test", "version": "1.0.0"}
