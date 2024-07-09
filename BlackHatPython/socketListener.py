import socket
import threading

def handle_connection(client_socket, client_address):
    # Обработка соединения
    print(f"Connection from {client_address}")
    data = client_socket.recv(1024)
    print(f"Recieved data: {data.decode('utf-8')}")
    # Закрытие соединения
    client_socket.close()

def main(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        # Создание отдельного потока для обработки каждого соединения
        client_thread = threading.Thread(
            target=handle_connection,
            args=(client_socket, client_address)
        )
        client_thread.start()

if __name__ == '__main__':
    print(main('127.0.0.1', 12345))