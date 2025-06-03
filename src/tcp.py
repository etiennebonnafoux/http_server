import socket 

class TCPServer :

    host = "0.0.0.0"
    port = 30000

    def start(self):

        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

            s.bind((self.host,self.port))

            s.listen(5)

            print("Listening at ",s.getsockname())

            while True:
                conn, addr = s.accept()
                with conn:

                        print("Connected by", addr)

                        data = conn.recv(1024)

                        print(f"Received: {data.decode()}")
                        conn.sendall(b"Additional data "+data)


if __name__ == "__main__":
    server = TCPServer()
    server.start()
