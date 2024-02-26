# Flake8: noqa;

import pytest
from flask import Flask

from src.factory import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True, "DEBUG": False})
    yield app


@pytest.fixture
def context(app: Flask):
    return app.app_context()


@pytest.fixture
def client(app: Flask):
    return app.test_client()


@pytest.fixture
def runner(app: Flask):
    return app.test_cli_runner()
