import socket
import threading

# Конфигурационные параметры для прокси
# Локальный порт, на котором будет работать прокси-сервер
LOCAL_PORT = 8080
# Удаленный хост (сервер), к которому будут перенаправляться запросы
REMOTE_HOST = 'example.com'
# Порт удаленного хоста
REMOTE_PORT = 80

def proxy_handler(client_socket):
    """ Обработчик соединения для прокси.
    Перенаправляет данные между клиентом и удаленнм сервером.
    """
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((REMOTE_HOST, REMOTE_PORT))

    while True:
        # Полученние данных от клиента и отправка на удаленный сервер
        data = client_socket.recv(4096)
        if not data:
            break
        remote_socket.sendall(data)

        # Получение ответа от удаленного сервера и отправка обратно клиенту
        response = remote_socket.recv(4096)
        if not response:
            break
        client_socket.sendall(response)
    # Закрытие соединений
    client_socket.close()
    remote_socket.close()

def main():
    """ Основная функия которая создает и запускает прокси-сервер. """
    # Создание сокета для сервера и привязка к локальному порту
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', LOCAL_PORT))
    server_socket.listen(5)
    print(f"Proxy server is listening on port {LOCAL_PORT}")

    try:
        # Основной цикл прослушивание для принятия соединения
        while True:
            client_socket, address = server_socket.accept()
            print(f"Accepted connection from {address}")
            # Запуск обработчика в отдельном потоке для каждого соединения
            client_thread = threading.Thread(target=proxy_handler, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print('Proxy server is shutting down.')
        server_socket.close()

if __name__ == '__main__':
    print(main())
