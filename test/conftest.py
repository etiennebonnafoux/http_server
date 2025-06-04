from pytest import fixture

@fixture(scope="session")
def well_formatted_http_packet():
    return b"""GET /index.html HTTP/1.1
            Host: example.com
            Connection: keep-alive
            User-Agent: Mozilla/5.0

            Hello Word"""

@fixture(scope="session")
def well_formatted_http_answer():
    return b"""HTTP/1.1 200 OK\r
Content-Type: text/plain\r
Content-Length: 10\r
\r
Hello Word"""