import socket
import time

from app_settings import *


def client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            client_socket.connect((TCP_IP, TCP_PORT))
            print(f'Run app')

            while True:
                message = input('--> ')
                if message.lower().strip() in ('end', 'stop', 'close', 'exit'):
                    print('App stopped')
                    break
                client_socket.send(message.encode())
                data = client_socket.recv(CHUNK_BYTES).decode()
                print(f'Received message: {data}')
    except (ConnectionResetError, BrokenPipeError, ConnectionRefusedError) as err:
        print(f'Connection was not established. {err}')


if __name__ == '__main__':
    client()
