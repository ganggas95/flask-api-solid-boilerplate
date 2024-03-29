from flask import Flask

from src.tests import BaseTestCase


class TestCreateFlask(BaseTestCase):

    def test_instance(self):
        self.assertIsInstance(self.app, Flask)

    def test_debug_mode(self):
        self.assertFalse(self.app.debug, "Ensure the app is not in debug mode")

    def test_healty(self):
        response = self.app.test_client().get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"pong")

    def test_container_should_be_defined(self):
        self.assertIsNotNone(self.app.container)
