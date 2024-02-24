import unittest

from flask import Flask

from src.factory import create_app


class TestCreateFlask(unittest.TestCase):
    app: Flask = None

    def setUp(self) -> None:
        self.app = create_app()
        return super().setUp()

    def test_instance(self):
        self.assertIsInstance(self.app, Flask)

    def test_debug_mode(self):
        self.assertFalse(self.app.debug, "Ensure the app is not in debug mode")

    def test_healty(self):
        response = self.app.test_client().get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"pong")
