import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_dir)

# import extensions  # noqa;
from blueprints import register_blueprints  # noqa;
from cli import init_cli  # noqa;
from config import get_config  # noqa;
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


def init_extension(app: FlaskWithContainer):
    """
    Initializes extensions for the given Flask app.
    Parameters:
        app (Flask): The Flask app to which the extensions
            will be added.
    Returns:
        None
    """
    ...


def create_app() -> FlaskWithContainer:
    """
    Create and return a new Flask application.

    Returns:
        Flask: A new instance of the Flask application.
    """
    app = FlaskWithContainer(__name__)
    app.config.from_object(get_config())
    app.container.config.from_dict(app.config)
    # init_extension(app)
    init_healty_route(app)
    register_blueprints(app)
    init_cli(app)
    return app


APP = create_app()
context = APP.app_context()
