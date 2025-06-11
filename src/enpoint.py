from typing import Callable
from src.constant import Methode
import inspect
from uuid import UUID
from datetime import datetime

class Endpoint:

    def __init__(self,funct :Callable,route:str,methode:Methode):
        self.funct = funct
        self.route = route
        self.methode = methode
        self.kwargs = self._compute_kwargs()

    def _compute_kwargs(self)-> inspect.Signature:
        res = inspect.signature(self.funct)
        for v in res.parameters.values():
            if v.annotation not in [str,int,bytes,float,UUID,datetime]:
                raise TypeError(f"Unsopported types {v.annotation}")
        return res
    
    def _validate_kwargs(self,**kwars) -> inspect.BoundArguments:
        return self.kwargs.bind(**kwars)

    def answer(self,**kwars):
        _ = self._validate_kwargs(**kwars)
        answer = self.funct(**kwars)
        return answer


