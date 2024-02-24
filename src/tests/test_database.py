import unittest
from unittest.mock import patch

from src.database import Database

database_url = "sqlite:///test.db"

with patch("src.database.create_engine") as mock_create_engine:

    class MockEngine:
        def connect(self):
            pass

    mock_create_engine.return_value.connect.return_value = MockEngine()

with patch("src.database.sessionmaker") as mock_sessionmaker:

    class MockSessionMaker:
        def __init__(self):
            pass

    mock_sessionmaker.return_value = MockSessionMaker()

with patch("src.database.scoped_session") as mock_scoped_session:

    class MockScoppedSession:
        def __init__(self):
            pass

    mock_scoped_session.return_value = MockScoppedSession()


class TestDatabase(unittest.TestCase):
    @patch("src.database.create_engine")
    def test_init_create_engine(self, mock_create_engine):
        db = Database(database_url)
        self.assertEqual(db._database_url, database_url)
        self.assertIsNotNone(db._engine)
        mock_create_engine.assert_called_with(database_url, connect_args={}, **{})

    @patch("src.database.sessionmaker")
    def test_init_session_maker(self, mock_sessionmaker):
        db = Database(database_url)
        self.assertEqual(db._database_url, database_url)
        self.assertIsNotNone(db._engine)
        mock_sessionmaker.assert_called_with(
            autoflush=False,
            autocommit=False,
            expire_on_commit=True,
            bind=db._engine,
        )

    @patch("src.database.scoped_session")
    def test_init_scoped_session(self, mock_scoped_session):
        db = Database(database_url)
        self.assertEqual(db._database_url, database_url)
        self.assertIsNotNone(db._session_maker)
        mock_scoped_session.assert_called_with(db._session_maker)

    def test_session(self):
        db = Database(database_url)
        session = db.session
        self.assertIsNotNone(session)
