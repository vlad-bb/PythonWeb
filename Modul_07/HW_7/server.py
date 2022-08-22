import socket
from concurrent.futures import ThreadPoolExecutor
from app_settings import *

ID = 0


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((TCP_IP, TCP_PORT))
        server_socket.listen(10)
        print(f'Start echo server {server_socket.getsockname()}')
        with ThreadPoolExecutor(10) as client_pool:
            while True:
                try:
                    new_sock, address = server_socket.accept()
                    client_pool.submit(handle, new_sock, address, get_id())
                except KeyboardInterrupt:
                    print(f'Destroy server')


def handle(conn: socket.socket, address: str, id_user: int):
    print(f'Connection User_{id_user} from {address}')
    with conn:
        while True:
            data = conn.recv(CHUNK_BYTES).decode()
            if not data:
                print(f'User_{id_user} stopped app')
                break
            print(f'received message from User_{id_user}: {data}')
            message = input(f'Answer to {id_user} --> ')
            conn.send(message.encode())


def get_id():
    global ID
    ID += 1
    return ID


if __name__ == '__main__':
    main()
