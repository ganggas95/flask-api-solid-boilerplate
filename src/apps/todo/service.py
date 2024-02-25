from typing import List, Union

from apps.todo.entity.dto import TodoDto
from apps.todo.entity.entity import TodoEntity
from apps.todo.repository import TodoRepository
from core.exceptions import BaseException
from core.types.http_status import HttpStatusCode


class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def get_all(self) -> List[TodoEntity]:
        return self.repository.get_all()

    def get(self, id: int, raise_notfound: bool = False) -> Union[TodoEntity, None]:
        todo = self.repository.get(id)
        if raise_notfound and not todo:
            raise BaseException(HttpStatusCode.NOT_FOUND, "Todo not found")
        return todo

    def add_todo(self, todo_dto: TodoDto) -> TodoEntity:
        todo = TodoEntity(**todo_dto)
        self.repository.save(todo)
        self.repository.commit()
        return todo

    def update_todo(self, id: int, todo_dto: TodoDto) -> TodoEntity:
        todo = self.get(id, raise_notfound=True)
        todo.title = todo_dto.get("title", todo.title)
        todo.completed = todo_dto.get("completed", todo.completed)
        self.repository.save(todo)
        self.repository.commit()
        return todo

    def delete_todo(self, id: int) -> None:
        todo = self.get(id, raise_notfound=True)
        self.repository.delete(todo)
        self.repository.commit()
