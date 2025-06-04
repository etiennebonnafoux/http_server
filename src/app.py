from typing import Callable
from src.constant import Methode,HTTPVersion,StatusCode
from src.parser import parse_message
from src.formatter import format_answer
import socket

class HttpApp:

    def __init__(self,host,port):
        self.endpoints : list[tuple[Callable,str,Methode]] = []
        self.host = host
        self.port = port
    
    def register_funtion(self,func : Callable,endpoint : str, methode : Methode):
        self.endpoints.append((func,endpoint,methode))

    def start(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

            s.bind((self.host,self.port))
            s.listen(5)
            while True:
                conn, addr = s.accept()
                with conn:


                        data = conn.recv(1024) #TODO retrouver la bonne fonction et l'appeller
                        meth,route,httpver,headers,content = parse_message(data)
                        match = False
                        for endpoint in self.endpoints:
                             if endpoint[1] == route  and endpoint[2] == meth:
                                answer = format_answer(HTTPVersion.HTTP11,StatusCode.OK200,{},f"Calling function {endpoint[0].__name__}")
                                conn.sendall(answer)
                                match = True
                                break
                        if not match:
                            answer = format_answer(HTTPVersion.HTTP11,StatusCode.NOT_FOUND404,{},"No matching function")
                            conn.sendall(answer)