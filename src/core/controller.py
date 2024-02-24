from typing import Any, Union

from dependency_injector.wiring import Provide, inject
from flask import Response, jsonify, make_response
from marshmallow import Schema

from container import DIContainer
from core.exceptions import BaseException
from core.types.db_session import ScopedSession
from core.types.http_status import HttpStatusCode


class BaseController:
    serializer_class: Union[Schema, None] = None

    @inject
    def response(
        self,
        data=None,
        message=None,
        status: HttpStatusCode = HttpStatusCode.OK,
        errors: Union[Any, None] = None,
        db_session: ScopedSession = Provide[DIContainer.db_session],
    ) -> Response:
        if self.serializer_class:
            data = self.serializer_class.dump(data)
        payload = jsonify(
            {"data": data, "message": message, "status": status, "errors": errors}
        )
        response = make_response(payload, status)
        # Close all db sessions
        if db_session:
            db_session.close_all()
        return response

    @inject
    def error_response(
        self,
        error: Union[Exception, BaseException],
        db_session: ScopedSession = Provide[DIContainer.db_session],
    ) -> Response:
        # Rollback the transaction and Close all db sessions
        if db_session:
            db_session.rollback()
            db_session.close_all()
        if isinstance(error, BaseException):
            return self.response(
                status=error.code, message=error.description, errors=error.errors
            )
        raise error
