from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise

from core.config import get_app_settings
from core.errors.http_error import http_error_handler
from core.errors.validation_error import http422_error_handler
from core.events import create_start_app_handler

from v1.api import router as v1_router


def get_application() -> FastAPI:

    settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # todo: add application.add_event_handler
    application.add_event_handler(
        "startup",
        create_start_app_handler(),
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(v1_router, prefix=settings.v1_prefix)

    # register tortoise-orm
    register_tortoise(
        application,
        # db_url="sqlite://test.sqlite3",
        db_url=settings.database_url,
        modules={"models": [
            "core.models.images",
            "core.models.albums",
            "core.models.users",
        ]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    return application

app = get_application()