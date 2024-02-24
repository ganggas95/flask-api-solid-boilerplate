from dependency_injector import containers, providers

from database import Database
from envs import DATABASE_CONNECT_ARGS, DATABASE_URL


class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["core"], packages=["core"]
    )
    config = providers.Configuration()

    db = providers.Singleton(
        Database, database_url=DATABASE_URL, **DATABASE_CONNECT_ARGS
    )

    db_session = providers.Singleton(db.provided.session)
