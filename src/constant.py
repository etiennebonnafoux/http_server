from enum import StrEnum,Enum

class StatusCode(Enum):
    OK200 = "200 OK"
    NOT_FOUND404 = "404 NOT FOUND"

class HTTPVersion(Enum):
    HTTP09 = "HTTP/0.9"
    HTTP10 = "HTTP/1.0"
    HTTP11 = "HTTP/1.1"
    HTTP2 = "HTTP/2"
    HTTP3 = "HTTP/3"

class Methode(StrEnum):
    GET = "GET"
    HEAD = "HEAD"
    OPTIONS = "OPTION"
    TRACE = "TRACE"
    PUT = "PUT"
    DELETE = "DELETE"
    POST = "POST"
    PATCH = "PATCH"
    CONNECT = "CONNECT"

