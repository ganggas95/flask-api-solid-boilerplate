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
