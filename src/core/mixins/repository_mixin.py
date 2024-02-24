from abc import ABC, abstractmethod
from functools import cached_property
from typing import Any, List, Union

from sqlalchemy.orm import Query

from core.types.db_session import ScopedSession

from ..entity import BaseType


class BaseRepositoryMixin(ABC):
    model_class: Union[BaseType, None] = None

    def __init__(self, db_session: ScopedSession) -> None:
        self.db_session = db_session

    def commit(self) -> None:
        self.db_session.commit

    def rollback(self) -> None:
        self.db_session.rollback()

    def save(self) -> None:
        self.db_session.add(self)

    def close(self) -> None:
        self.db_session.close()

    @cached_property
    def query(self) -> Query:
        return self.db_session.query(self.model_class)


class BaseRepositoryWithCRUDMixin(BaseRepositoryMixin, ABC):
    @abstractmethod
    def get(self, id: int) -> Union[Any, None]: ...

    @abstractmethod
    def get_all(self) -> List[Any]: ...

    @abstractmethod
    def create(self, data: Any) -> Any: ...

    @abstractmethod
    def update(self, id: int, data: Any) -> Any: ...

    @abstractmethod
    def delete(self, id: int) -> Any: ...
