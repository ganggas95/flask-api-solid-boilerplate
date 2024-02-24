from typing import Type

from sqlalchemy.orm import declarative_base

Base = declarative_base()

BaseType = Type[Base]
