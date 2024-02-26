from typing import Dict

from flask_restx import Namespace, fields

todo_create_model = {
    "title": fields.String(required=True),
    "completed": fields.Boolean(allow_none=True, default=False),
}

todo_update_model = {
    "title": fields.String(allow_none=True, required=False),
    "completed": fields.Boolean(allow_none=True, default=False),
}


def initilize_model(namespace: Namespace) -> Dict[str, object]:
    return {
        "create": namespace.model("CreateTodo", todo_create_model),
        "update": namespace.model("UpdateTodo", todo_update_model),
    }
