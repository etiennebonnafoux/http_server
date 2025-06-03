from src.parser import parse_message
from src.constant import Methode

def test_parser(well_formatted_http_packet: bytes):
    meth,route,proto,header,content = parse_message(well_formatted_http_packet)
    assert meth == Methode.GET
    assert route == "/index.html"
    assert proto == "HTTP/1.1"
    assert "User-Agent" in header
    assert "Mozilla/5.0" in header.values()
    assert content == b"Hello Word"