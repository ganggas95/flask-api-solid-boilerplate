import os
import sys

from flask import Flask

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_dir)


def ping():
    return "pong"


def init_healty_route(app: Flask) -> None:
    """
    Initializes a health check route for the given Flask app.
    Parameters:
        app (Flask): The Flask app to which the health check
            route will be added.
    Returns:
        None
    """
    app.add_url_rule("/ping", view_func=ping)


def create_app() -> Flask:
    """
    Create and return a new Flask application.

    Returns:
        Flask: A new instance of the Flask application.
    """
    app = Flask(__name__)
    init_healty_route(app)
    return app


APP = create_app()
context = APP.app_context()
