import unittest
from typing import Union

from flask.testing import FlaskClient

from core.flask import FlaskWithContainer
from factory import create_app


class BaseTestCase(unittest.TestCase):
    app: Union[FlaskWithContainer, None] = None
    client: Union[FlaskClient, None] = None

    def setUp(self) -> None:
        self.app = create_app()
        with self.app.app_context():
            self.app.db.create_database()
        self.client = self.app.test_client()
        return super().setUp()

    def tearDown(self) -> None:
        self.app.db.drop_database()
        return super().tearDown()
