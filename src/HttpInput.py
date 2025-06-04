from typing import Self
from src.constant import Methode,HTTPVersion
from dataclasses import dataclass
import json

class ParsingException(Exception): ...

@dataclass
class HTTPInput:

    methode : Methode
    route : str
    http_version : HTTPVersion
    headers : dict[str,str]
    content : bytes


    @classmethod
    def from_bytes(data:bytes) -> "HTTPInput":
        
        """Parse the received data

        Returns:
            tuple[Methode,HTTPVersion,str,dict[str,Any],bytes]: The Methode,HTTP Version,route,header and content
        """
        message = data.decode()
        lines = message.splitlines()
        try:
            mandatory_line = lines[0]
        except IndexError:
            raise ParsingException("Empty data")
        lines.pop(0)
        meth, route, protocol = parse_first_line(mandatory_line)
        header = {}
        contents = []
        finish_header = False
        for line in lines:
            if line.strip() == '':
                finish_header = True
            if finish_header:
                contents.append(line)
            else:
                key_value = line.split(":")
                header[key_value[0].strip()] = key_value[1].strip()
        return HTTPInput(meth, route, protocol, header, "\n".join(contents).strip().encode())

    def decode_content(self):
        if "Content-Type" in self.headers.keys():
            if self.headers["Content-Type"] == "application/json":        
                return json.load(self.content.decode())


def parse_first_line(line: str) -> tuple[Methode, str, HTTPVersion]:
    meth,route,httpvr = line.split()
    return Methode(meth),route,HTTPVersion(httpvr)