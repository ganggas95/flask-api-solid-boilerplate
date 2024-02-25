from flask_restx import Namespace

from apps.todo.mixin import TodoControllerMixin
from apps.todo.schema.serializers import TodoSerializers
from core.mixins.controller_mixin import (BaseControllerMixin,
                                          ControllerValidatorMixin)
from core.types.http_status import HttpStatusCode

from .schema.request import todo_create_model, todo_update_model

namespace = Namespace("", description="Todo related operations", tags="Todo")

create_model = namespace.model("CreateTodo", todo_create_model)
update_model = namespace.model("UpdateTodo", todo_update_model)


@namespace.route("/list", endpoint="list")
class ListTodoController(TodoControllerMixin, BaseControllerMixin):
    serializer_class = TodoSerializers(many=True)

    @namespace.doc(name="Get all todos", description="Get all todos")
    def get(self):
        try:
            return self.response(
                data=self._todo_service.get_all(),
                message="Todos retrieved successfully",
            )
        except Exception as e:
            return self.error_response(e)


@namespace.route("/add", endpoint="create")
class CreateTodoController(TodoControllerMixin, ControllerValidatorMixin):
    serializer_class = TodoSerializers()

    @namespace.doc(model=create_model, body=create_model)
    @namespace.expect(create_model, validate=True)
    def post(self):
        try:
            todo = self._todo_service.add_todo(self.payload)
            return self.response(
                data=todo,
                status=HttpStatusCode.CREATED,
                message="Todo created successfully",
            )
        except Exception as e:
            return self.error_response(e)


@namespace.route("/<int:id>/detail")
@namespace.doc(params={"id": "ID of todo"})
class DetailTodoController(TodoControllerMixin, ControllerValidatorMixin):
    serializer_class = TodoSerializers()

    def get(self, id):
        try:
            return self.response(
                data=self._todo_service.get(id),
                message="Todo retrieved successfully",
            )
        except Exception as e:
            return self.error_response(e)

    @namespace.doc(model=update_model, body=update_model)
    @namespace.expect(update_model)
    def put(self, id):
        try:
            todo = self._todo_service.update_todo(id, self.payload)
            return self.response(
                data=todo,
                status=HttpStatusCode.OK,
                message="Todo updated successfully",
            )
        except Exception as e:
            return self.error_response(e)

    def delete(self, id):
        try:
            self._todo_service.delete_todo(id)
            return self.response(
                status=HttpStatusCode.NO_CONTENT, message="Todo deleted successfully"
            )
        except Exception as e:
            return self.error_response(e)
