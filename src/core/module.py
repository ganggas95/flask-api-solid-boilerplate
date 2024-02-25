from flask import Blueprint, Flask
from flask_restx import Api


class Module(Blueprint):
    def __init__(
        self, name: str, swagger_title: str, url_prefix: str, *args, **kwargs
    ):
        super().__init__(name, __name__, url_prefix=url_prefix, *args, **kwargs)
        self._api = Api(self, title=swagger_title, version="1.0", doc="/docs")

    def add_namespace(self, namespace: Api):
        self._api.add_namespace(namespace)

    def init_app(self, app: Flask):
        app.register_blueprint(self)
