from typing import Any

from werkzeug.exceptions import HTTPException

from core.types.http_status import HTTP_STATUS_MESSAGE_MAP, HttpStatusCode


class BaseException(HTTPException):
    errors = None

    def __init__(
        self,
        code: HttpStatusCode,
        description: str | None = None,
        errors: Any | None = None,
    ) -> None:
        self.code = code
        self.errors = errors
        self.description = description or HTTP_STATUS_MESSAGE_MAP[code]
        super().__init__(description)
