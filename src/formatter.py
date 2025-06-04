from src.constant import StatusCode,HTTPVersion

def format_answer(httpvrs : HTTPVersion,status_code: StatusCode,header:dict[str,str],content:str) -> bytes:
    answer = f"{httpvrs.value} {status_code.value}\r\n"
    content_bytes = content.encode('utf-8') # Assume UTF-8 for content encoding
    header['Content-Length'] = str(len(content_bytes))
    if 'Content-Type' not in header: # Only add if not already present
        header['Content-Type'] = 'text/plain; charset=utf-8'
    answer += "\r\n".join(f"{k}: {v}" for k,v in header.items())
    answer += "\r\n\r\n"
    answer += content
    return answer.encode()
        