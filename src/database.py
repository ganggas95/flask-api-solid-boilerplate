from functools import cached_property
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from core.types.db_session import ScopedSession


class Database:
    def __init__(
        self, database_url: str, connect_args: Union[dict, None] = {}, **kwargs
    ) -> None:
        self.database_url = database_url
        self.engine = create_engine(
            self.database_url,
            connect_args=connect_args,
            echo=True,
            **kwargs,
        )
        self.session_maker = sessionmaker(
            autoflush=False,
            autocommit=False,
            expire_on_commit=True,
            bind=self.engine,
        )
        self.session_factory = scoped_session(self.session_maker)

    def create_database(self) -> None:
        from core.entity import Base

        Base.metadata.create_all(self.engine)

    def drop_database(self) -> None:
        from core.entity import Base

        Base.metadata.drop_all(self.engine)

    @cached_property
    def session(self) -> ScopedSession:
        """
        A property decorator that caches the result of the session method
            and returns the scoped session.
        """
        return Session(self.engine)
