from src.parser import parse_message
from src.constant import Methode,HTTPVersion

def test_parser(well_formatted_http_packet: bytes):
    meth,route,proto,header,content = parse_message(well_formatted_http_packet)
    assert meth == Methode.GET
    assert route == "/index.html"
    assert proto == HTTPVersion.HTTP11
    assert "User-Agent" in header
    assert "Mozilla/5.0" in header.values()
    assert content == b"Hello Word"