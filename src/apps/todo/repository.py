from typing import List, Union

from apps.todo.entity import TodoEntity
from core.mixins.repository_mixin import BaseRepositoryMixin


class TodoRepository(BaseRepositoryMixin):
    model_class = TodoEntity

    def get_all(self) -> List[TodoEntity]:
        with self.db_session as session:
            return session.execute(self.select).scalars().all()

    def get(self, id: int) -> Union[TodoEntity, None]:
        with self.db_session as session:
            return session.get(self.model_class, id)
