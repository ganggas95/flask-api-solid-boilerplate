from datetime import datetime
from typing import Type

from sqlalchemy import DateTime, Integer, func
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()

BaseType = Type[Base]


class BaseEntityWithIdInteger(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class BaseTimestampEntity(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), server_onupdate=func.now()
    )
