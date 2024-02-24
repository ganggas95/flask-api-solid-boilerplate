from flask import Flask

from container import DIContainer


class FlaskWithContainer(Flask):
    container: DIContainer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = DIContainer()
