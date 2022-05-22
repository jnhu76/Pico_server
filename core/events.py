from typing import Callable

from core.services.storage.minio import create_bucket


def create_start_app_handler() -> Callable:  # type: ignore
    def start_app() -> None:
        create_bucket()

    return start_app
