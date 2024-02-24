from flask import Flask


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
