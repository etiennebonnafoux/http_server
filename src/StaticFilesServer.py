from pathlib import Path
from src.formatter import format_answer
from src.constant import HTTPVersion,StatusCode

class StaticFilesServer:
    def __init__(self,folder:Path):
        self.folder = folder

    def serve_file(self,file:str) -> bytes:
        path_file = self.folder / Path(file)
        if not path_file.exists() : 
            return format_answer(HTTPVersion.HTTP11,StatusCode.NOT_FOUND404,{},content="Not found")
        with open(path_file,"r") as f:
            content = f.read()
        return format_answer(HTTPVersion.HTTP11,StatusCode.OK200,{},content=content)