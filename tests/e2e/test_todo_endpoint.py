from json import loads

from apps.todo.entity import TodoEntity
from core.types.http_status import HttpStatusCode
from src.tests import BaseTestCase


class TestTodoEndpoint(BaseTestCase):
    todo: TodoEntity = None

    def setUp(self) -> None:
        super().setUp()
        self.todo_repository = self.app.container.todo_repository.provided()
        self.todo_service = self.app.container.todo_service.provided()
        self.init_data()

    def init_data(self):
        todo = TodoEntity(title="Test title", completed=False)
        self.todo_repository.save(todo)
        self.todo_repository.commit()
        self.todo = todo

    def test_1_GET_list_todos_success(self):
        # Exercise
        response = self.client.get("/api/v1/todo/list")

        # Verify
        self.assertEqual(response.status_code, HttpStatusCode.OK)

    def test_2_POST_add_todo_success(self):
        # Setup
        payload = '{"title": "Test title", "completed": false}'

        # Exercise
        response = self.client.post("/api/v1/todo/add", json=loads(payload))
        response_data = response.get_json()
        data = response_data["data"]

        # Verify
        self.assertEqual(data["title"], "Test title")
        self.assertFalse(data["completed"])
        self.assertIsNotNone(data["id"])
        self.assertEqual(response.status_code, HttpStatusCode.CREATED)

    def test_3_POST_add_todo_fail(self):
        # Setup
        payload = '{"completed": false}'

        # Exercise
        response = self.client.post("/api/v1/todo/add", json=loads(payload))
        response_data = response.get_json()
        errors = response_data["errors"]

        # Verify
        self.assertIsNotNone(errors, None)
        self.assertEqual(response.status_code, HttpStatusCode.BAD_REQUEST)

    def test_4_GET_detail_todo_success(self):
        # Exercise
        response = self.client.get(f"/api/v1/todo/{self.todo.id}/detail")

        # Verify
        self.assertEqual(response.status_code, HttpStatusCode.OK)

    def test_5_PUT_update_todo_success(self):
        # Setup
        payload = '{"title": "Test title", "completed": true}'

        # Exercise
        response = self.client.put(
            f"/api/v1/todo/{self.todo.id}/detail", json=loads(payload)
        )
        response_data = response.get_json()
        data = response_data["data"]

        # Verify
        self.assertEqual(data["title"], "Test title")
        self.assertTrue(data["completed"])
        self.assertEqual(data["id"], self.todo.id)
        self.assertEqual(response.status_code, HttpStatusCode.OK)

    def test_5_PUT_update_todo_fail(self):
        # Setup
        payload = "{}"

        # Exercise
        response = self.client.put("/api/v1/todo/-1/detail", json=loads(payload))
        # Verify
        self.assertEqual(response.status_code, HttpStatusCode.NOT_FOUND)

    def test_6_DELETE_delete_todo_success(self):
        # Exercise
        response = self.client.delete(f"/api/v1/todo/{self.todo.id}/detail")

        # Verify
        self.assertEqual(response.status_code, HttpStatusCode.NO_CONTENT)
