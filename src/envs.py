import os
from pathlib import Path

from dotenv import load_dotenv

ENV = os.getenv("ENV", "development")

ENV_MAP = {
    "development": ".env.development",
    "testing": ".env.test",
    "production": ".env.production",
}

env_path = Path(".") / ENV_MAP[ENV]
load_dotenv(dotenv_path=env_path)


DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_POOL_SIZE = int(os.getenv("DATABASE_POOL_SIZE", 5))
DATABASE_POOL_TIMEOUT = int(os.getenv("DATABASE_POOL_TIEMOUT", 10))
DATABASE_CONNECT_ARGS = {
    "pool_size": DATABASE_POOL_SIZE,
    "pool_timeout": DATABASE_POOL_TIMEOUT,
}
