import enum

ALLOWED_HTTP_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


class HTTPMethods(enum.Enum):
    get = "GET"
    post = "POST"
    patch = "PATCH"
    put = "PUT"
    delete = "DELETE"
