import socket

def run_tcp_client():
    host = '127.0.0.1'
    port = 30000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            message = "Hello from the TCP client!"
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")
        except ConnectionRefusedError:
            print("Connection to server refused.")

if __name__ == "__main__":
    run_tcp_client()