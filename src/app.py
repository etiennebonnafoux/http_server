from typing import Callable
from src.constant import Methode, HTTPVersion, StatusCode
from src.formatter import format_answer
from src.enpoint import Endpoint
from src.HttpInput import HTTPInput
from src.middelware import MiddelWare
from src.StaticFilesServer import StaticFilesServer
import socket
from pathlib import Path


class HttpApp:
    def __init__(self, host : str, port : int):
        self.endpoints: list[Endpoint] = []
        self.middelware: list[MiddelWare] = []
        self.static_file_handlers : list[StaticFilesServer] = []
        self.host = host
        self.port = port

    def register_funtion(self, func: Callable, endpoint: str, methode: Methode):
        self.endpoints.append(Endpoint(func, endpoint, methode))

    def add_static_folder(self,path:Path):
        self.static_file_handlers.append(StaticFilesServer(folder=path))

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(5)
            print("Listening")
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(
                        1024
                    )  # TODO retrouver la bonne fonction et l'appeller
                    http_input : HTTPInput = HTTPInput.from_bytes(data)
                    match = False
                    for endpoint in self.endpoints:
                        if endpoint.route == http_input.route and endpoint.methode == http_input.methode :
                            try:
                                answer_content = endpoint.answer(http_input.decode_content())
                                answer = format_answer(
                                    HTTPVersion.HTTP11,
                                    StatusCode.OK200,
                                    {},
                                    f"{answer_content}",
                                )
                                conn.sendall(answer)
                            except TypeError:
                                answer_content = format_answer(HTTPVersion.HTTP11,StatusCode.UNPROCESSABLE422,{},"Arguments does not match")
                            match = True
                            break
                    if not match:
                        answer = format_answer(
                            HTTPVersion.HTTP11,
                            StatusCode.NOT_FOUND404,
                            {},
                            "No matching function",
                        )
                        conn.sendall(answer)
