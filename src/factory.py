import os
import sys

from flask import Flask

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_dir)


def create_flask() -> Flask:
    """
    Create and return a new Flask application.

    Returns:
        Flask: A new instance of the Flask application.
    """
    app = Flask(__name__)
    return app


APP = create_flask()
context = APP.app_context()
