import unittest

from flask import Flask

from src.factory import create_flask


class TestCreateFlask(unittest.TestCase):
    def create_app(self):
        return create_flask()

    def test_instance(self):
        self.assertIsInstance(self.app, Flask)

    def test_debug_mode(self):
        self.assertFalse(self.app.debug, "Ensure the app is not in debug mode")
