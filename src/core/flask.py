from flask import Flask

from container import DIContainer
from database import Database


class FlaskWithContainer(Flask):
    container: DIContainer
    db: Database

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = DIContainer()
        self.db = self.container.db.provided()
