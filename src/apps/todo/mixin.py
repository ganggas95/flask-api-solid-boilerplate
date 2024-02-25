from dependency_injector.wiring import Provide, inject
from flask_restx import Resource

from container import DIContainer

from .service import TodoService


class TodoControllerMixin(Resource):
    @inject
    def __init__(
        self,
        api=None,
        service: TodoService = Provide[DIContainer.todo_service],
        *args,
        **kwargs
    ):

        super().__init__(api, *args, **kwargs)
        self._todo_service = service
