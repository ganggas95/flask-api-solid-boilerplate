from dependency_injector import containers, providers

from apps.todo.repository import TodoRepository
from apps.todo.service import TodoService
from database import Database
from envs import DATABASE_CONNECT_ARGS, DATABASE_URL


class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["core", "apps.todo.mixin"], packages=["core"]
    )
    config = providers.Configuration()

    db = providers.Singleton(
        Database, database_url=DATABASE_URL, **DATABASE_CONNECT_ARGS
    )

    db_session = providers.Singleton(db.provided.session)

    todo_repository = providers.Factory(TodoRepository, db_session=db_session)

    todo_service = providers.Factory(TodoService, repository=todo_repository)
