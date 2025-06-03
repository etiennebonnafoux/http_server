from enum import StrEnum

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

