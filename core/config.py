from functools import lru_cache
from typing import Dict, Type


from core.settings.app import AppSettings
from core.settings.base import AppEnvTypes, BaseAppSettings
from core.settings.dev import DevAppSettings
from core.settings.prod import ProdAppSettings
from core.settings.test import TestAppSettings


environment: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environment[app_env]
    return config()
