from functools import cached_property
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from core.types.db_session import ScoppedSession


class Database:
    def __init__(
        self, database_url: str, connect_args: Union[dict, None] = {}, **kwargs
    ) -> None:
        self._database_url = database_url
        self._engine = create_engine(
            self._database_url,
            connect_args=connect_args,
            **kwargs,
        )
        self._session_maker = sessionmaker(
            autoflush=False,
            autocommit=False,
            expire_on_commit=True,
            bind=self._engine,
        )
        self._session_factory = scoped_session(self._session_maker)

    def create_database(self) -> None:
        from core.entity import Base

        Base.metadata.create_all(self._engine)

    def drop_database(self) -> None:
        from core.entity import Base

        Base.metadata.drop_all(self._engine)

    @cached_property
    def session(self) -> ScoppedSession:
        """
        A property decorator that caches the result of the session method
            and returns the scoped session.
        """
        return self._session_factory
