from core.module import Module

from .controller import namespace

todo_module = Module("Todo", swagger_title="Todo API", url_prefix="/api/v1/todo")
todo_module.add_namespace(namespace)
