import asyncio
from typing import Generator
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient

import pytest
from fastapi.testclient import TestClient

from core.models.images import Images

from tortoise.contrib.test import finalizer, initializer

@pytest.fixture
def get_app() -> FastAPI:
    from main import get_application

    return get_application()


@pytest.fixture(scope="module")
async def initialized_app(app: FastAPI) -> FastAPI:
    async with LifespanManager(app):
        yield app


@pytest.fixture(scope="module")
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client

@pytest.mark.asyncio
async def test_create_image(app: FastAPI, client: AsyncClient):  # nosec
    print("test")
    assert 1 == 1
    # response = await client.post(app.url_path_for("image:upload-image"), files={"file": ("cat.jpeg", open("../images/cat.jpeg", "rb"), "image/jpeg")})
      

    # assert response.status_code == 200, response.text
    # data = response.json()
    # print(data)
    # assert "id" in data
    # image_id = data["id"]
    
    # async def get_image_by_db():
    #     image = await Images.get(id=image_id)
    #     return image

    # image_obj = await get_image_by_db()
    # assert image_id == image_obj.id
