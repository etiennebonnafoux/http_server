from enum import StrEnum

class Methode(StrEnum):
    GET = "get"
    HEAD = "head"
    OPTIONS = "option"
    TRACE = "trace"
    PUT = "put"
    DELETE = "delete"
    POST = "post"
    PATCH = "patch"
    CONNECT = "connect"

