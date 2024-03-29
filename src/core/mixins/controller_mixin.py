from functools import cached_property
from typing import Any, TypeVar, Union

from dependency_injector.wiring import Provide, inject
from flask import Request, Response, jsonify, make_response, request
from marshmallow import Schema

from container import DIContainer
from core.exceptions import BaseException
from core.types.db_session import ScopedSession
from core.types.http_status import HttpStatusCode

_T = TypeVar("_T", bound=Schema)


class BaseControllerMixin:
    serializer_class: Union[Schema, None] = None

    @cached_property
    def request(self) -> Request:
        return request

    @inject
    def response(
        self,
        data=None,
        message=None,
        status: HttpStatusCode = HttpStatusCode.OK,
        errors: Union[Any, None] = None,
        db_session: ScopedSession = Provide[DIContainer.db_session],
    ) -> Response:
        """
        Send a HTTP response with the given data and status code.

        The method serializes the provided data using the controller's serializer
        class if one is defined, constructs a JSON payload, and creates a Flask
        response object with the status code. It also handles the closing of the
        database session after the response is constructed.

        Args:
            data: The data to be included in the response, which will be serialized
                if a serializer class is set for the controller.
            message: An optional message to include in the response.
            status: The HTTP status code for the response. Defaults to
                HttpStatusCode.OK.
            errors: Any errors to include in the response.
            db_session: The database session to be used and closed after the response
                        is made. Provided by dependency injection.

        Returns:
            A Flask Response object containing the JSON payload.
        """
        if self.serializer_class:
            data = self.serializer_class.dump(data)
        payload = jsonify({"data": data, "message": message, "errors": errors})
        response = make_response(payload, status)
        # Close all db sessions
        if db_session:
            db_session.close()
        return response

    @inject
    def error_response(
        self,
        error: Union[Exception, BaseException],
        db_session: ScopedSession = Provide[DIContainer.db_session],
    ) -> Response:
        """
        Handles error responses by rolling back the database session and closing it.
        If the error is an instance of BaseException, it constructs a response
        with the error details.

        Args:
            error: The error that occurred. Must be an instance of Exception or
                BaseException.
            db_session: The database session in use, which will be rolled back and
                closed. This is provided by dependency injection.

        Returns:
            A Flask Response object with the error details if the error is a
                BaseException.
            Otherwise, the error is raised and should be handled by an outer
                exception handler.

        Raises:
            error: The original error if it is not an instance of BaseException.
        """
        # Rollback the transaction and Close all db sessions
        if db_session:
            db_session.rollback()
            db_session.close()
        if isinstance(error, BaseException):
            return self.response(
                status=error.code, message=error.description, errors=error.errors
            )
        raise error


class ControllerValidatorMixin(BaseControllerMixin):
    validator_schema = None

    @cached_property
    def payload(self):
        if self.request.is_json:
            return self.request.get_json(force=True)
        return self.request.form

    @cached_property
    def files(self):
        return self.request.files

    def _get_validator_class(self) -> _T:
        if self.validator_schema is None:
            raise Exception(
                f"type of validator_schema is Schema, {type(self.validator_schema)} given"  # NOQA
            )
        return self.validator_schema

    def _get_validator(self, *args, **kwargs) -> _T:
        validator_class = self._get_validator_class()
        return validator_class(*args, **kwargs)

    def validate(self, *args, **kwargs) -> _T:
        validator = self._get_validator(*args, **kwargs)
        errors = validator.validate(self.payload)
        if bool(errors):
            raise BaseException(HttpStatusCode.BAD_REQUEST, errors=errors)
        return self.payload
