from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from core.entity import BaseEntityWithIdInteger, BaseTimestampEntity


class TodoEntity(BaseEntityWithIdInteger, BaseTimestampEntity):
    __tablename__ = "tb_todos"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f"<TodoEntity(id={self.id}, title={self.title}, completed={self.completed})>"  # NOQA
