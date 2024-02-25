from flask_restx import fields

todo_create_model = {
    "title": fields.String(required=True),
    "completed": fields.Boolean(allow_none=True, default=False),
}

todo_update_model = {
    "title": fields.String(allow_none=True, required=False),
    "completed": fields.Boolean(allow_none=True, default=False),
}
