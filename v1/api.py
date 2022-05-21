from fastapi import APIRouter

from v1.endpoints import images

router = APIRouter()

router.include_router(images.router, tags=["images"])


@router.get("")
async def hello() -> str:
    return "hello world"
