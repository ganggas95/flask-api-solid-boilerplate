import os

from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")
DATABASE_POOL_SIZE = os.getenv("DATABASE_POOL_SIZE", 5)
DATABASE_POOL_TIMEOUT = os.getenv("DATABASE_POOL_TIEMOUT", 10)
DATABASE_CONNECT_ARGS = {
    "pool_size": DATABASE_POOL_SIZE,
    "pool_timeout": DATABASE_POOL_TIMEOUT,
}
