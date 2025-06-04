from src.app import HttpApp
from src.constant import Methode

app = HttpApp(host="0.0.0.0",port=30000)

def hello():
    return "Hello"

app.register_funtion(hello,"/hello",Methode.GET)

if __name__ == "__main__":
    app.start()