from src.formatter import format_answer
from src.constant import StatusCode,HTTPVersion

def test_parser(well_formatted_http_answer: bytes):
    header = {"Content-Type":"text/plain"}
    content = "Hello Word"
    answer = format_answer(HTTPVersion.HTTP11,StatusCode.OK200,header,content)
    assert answer == well_formatted_http_answer