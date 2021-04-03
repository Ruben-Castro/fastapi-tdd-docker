from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

# basically the same thing as Blueprint in flask
router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
