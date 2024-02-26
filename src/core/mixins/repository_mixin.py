from abc import ABC, abstractmethod
from functools import cached_property
from typing import Any, List, Union

from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from ..entity import BaseType


class BaseRepositoryMixin(ABC):
    model_class: Union[BaseType, None] = None

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def commit(self) -> None:
        self.db_session.commit()

    def rollback(self) -> None:
        self.db_session.rollback()

    def save(self, entity: Any, commit: bool = False) -> None:
        self.db_session.add(entity)
        if commit:
            self.commit()

    def close(self) -> None:
        self.db_session.close()

    def delete(self, entity: Any, commit: bool = False) -> None:
        self.db_session.delete(entity)
        if commit:
            self.commit()

    @cached_property
    def select(self) -> Select[BaseType]:
        if self.model_class is None:
            raise Exception("model_class must be set")
        return select(self.model_class)

    @abstractmethod
    def get(self, id: int) -> Union[Any, None]: ...

    @abstractmethod
    def get_all(self) -> List[Any]: ...

    def create(self, data: Any) -> Any:
        if self.model_class is None:
            raise Exception("model_class must be set")
        return self.model_class(**data)
