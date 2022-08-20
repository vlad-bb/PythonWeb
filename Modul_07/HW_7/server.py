import socket
from app_settings import *


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((TCP_IP, TCP_PORT))
        print(f'Run server, port: {TCP_PORT}')
        server_socket.listen(1)
        conn, address = server_socket.accept()
        print(f'Connection from {address}')
        with conn:
            while True:
                data = conn.recv(CHUNK_BYTES).decode()
                if not data:
                    print('User stopped app')
                    break
                print(f'received message: {data}')
                message = input('--> ')
                conn.sendall(message.encode())


if __name__ == '__main__':
    main()
