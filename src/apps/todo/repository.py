from typing import List, Union

from apps.todo.entity.entity import TodoEntity
from core.mixins.repository_mixin import BaseRepositoryMixin


class TodoRepository(BaseRepositoryMixin):
    model_class = TodoEntity

    def get_all(self) -> List[TodoEntity]:
        return self.query.all()

    def get(self, id: int) -> Union[TodoEntity, None]:
        return self.query.get(id)
