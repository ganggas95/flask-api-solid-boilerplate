from flask import Flask

from apps.todo.module import todo_module


def register_blueprints(app: Flask) -> None:
    todo_module.init_app(app)
