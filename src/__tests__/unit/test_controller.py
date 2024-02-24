from core.exceptions import BaseException
from core.mixins.controller_mixin import BaseControllerMixin
from core.types.http_status import HttpStatusCode


def test_response(context):
    # Setup
    controller = BaseControllerMixin()
    controller.serializer_class = None
    data = {"key": "value"}
    message = "Test message"
    status = HttpStatusCode.OK
    errors = None

    # Exercise
    with context:
        response = controller.response(data, message, status, errors)

    # Verify
    assert response is not None


def test_error_response(context):
    # Setup
    controller = BaseControllerMixin()
    error = BaseException(code=HttpStatusCode.BAD_REQUEST, errors="Test error")
    error.code = 500
    error.description = "Test error description"
    error.errors = "Test error"

    # Exercise
    with context:
        response = controller.error_response(error)

    # Verify
    assert response is not None
