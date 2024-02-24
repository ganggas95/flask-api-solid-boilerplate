import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_dir)

from core.flask import FlaskWithContainer  # noqa;


def init_healty_route(app: FlaskWithContainer) -> None:
    """
    Initializes a health check route for the given Flask app.
    Parameters:
        app (Flask): The Flask app to which the health check
            route will be added.
    Returns:
        None
    """
    app.add_url_rule("/ping", view_func=lambda: "pong")


def create_app() -> FlaskWithContainer:
    """
    Create and return a new Flask application.

    Returns:
        Flask: A new instance of the Flask application.
    """
    app = FlaskWithContainer(__name__)
    init_healty_route(app)
    return app


APP = create_app()
context = APP.app_context()
