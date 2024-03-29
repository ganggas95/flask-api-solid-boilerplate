from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from apps.todo.entity import TodoEntity


class TodoSerializers(SQLAlchemyAutoSchema):

    class Meta:
        model = TodoEntity
