from src.constant import StatusCode,HTTPVersion

def format_answer(httpvrs : HTTPVersion,status_code: StatusCode,header:dict[str,str],content:str) -> bytes:
    answer = f"{httpvrs.value} {status_code.value}\n"
    answer += "\n".join(f"{k} : {v}" for k,v in header.items())
    answer += "\n\n"
    answer += content
    return answer.encode()
        