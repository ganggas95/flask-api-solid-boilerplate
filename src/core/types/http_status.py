from typing import Dict


class HttpStatusCode:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GONE = 410
    UNPROCESSABLE_ENTITY = 422
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    REQUEST_TIMEOUT = 408
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    REQUESTED_RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417


HTTP_STATUS_MESSAGE_MAP: Dict[int, str] = {
    HttpStatusCode.OK: "OK",
    HttpStatusCode.CREATED: "Created",
    HttpStatusCode.ACCEPTED: "Accepted",
    HttpStatusCode.NO_CONTENT: "No Content",
    HttpStatusCode.BAD_REQUEST: "Bad Request",
    HttpStatusCode.UNAUTHORIZED: "Unauthorized",
    HttpStatusCode.FORBIDDEN: "Forbidden",
    HttpStatusCode.NOT_FOUND: "Not Found",
    HttpStatusCode.CONFLICT: "Conflict",
    HttpStatusCode.INTERNAL_SERVER_ERROR: "Internal Server Error",
    HttpStatusCode.BAD_GATEWAY: "Bad Gateway",
    HttpStatusCode.SERVICE_UNAVAILABLE: "Service Unavailable",
    HttpStatusCode.GONE: "Gone",
    HttpStatusCode.UNPROCESSABLE_ENTITY: "Unprocessable Entity",
    HttpStatusCode.TOO_MANY_REQUESTS: "Too Many Requests",
    HttpStatusCode.REQUEST_HEADER_FIELDS_TOO_LARGE: "Request Header Fields Too Large",  # noqa
    HttpStatusCode.UNAVAILABLE_FOR_LEGAL_REASONS: "Unavailable For Legal Reasons",
    HttpStatusCode.METHOD_NOT_ALLOWED: "Method Not Allowed",
    HttpStatusCode.NOT_ACCEPTABLE: "Not Acceptable",
    HttpStatusCode.REQUEST_TIMEOUT: "Request Timeout",
}
