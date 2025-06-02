from typing import Any
from constant import Methode

class ParsingException(Exception):
    ...

def parse_message(data : bytes) -> tuple[Methode,str,str,dict[str,Any],bytes]:
    """Parse the received data

    Returns:
        tuple[Methode,str,str,dict[str,Any],bytes]: The Methode,route,protocol,header and content
    """
    pass