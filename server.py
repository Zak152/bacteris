import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Настройка сокета
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Отключение пакетрования
main_socket.bind(('localhost', 10000))  # IP и привязка к порту
main_socket.setblocking(False)  # Непрерывность, не ждём ответа
main_socket.listen(5)  # Включение прослушивания, 5 - максимальное кол-во соединений
print('Сокет создался')

players = []
while True:
    try:
        new_socket, adress = main_socket.accept()
        print(f'Соединение установлено с {adress}')
        new_socket.setblocking(False)
        players.append(new_socket)

    except BlockingIOError:
        pass
    for sock in players:
        try:
            data = sock.recv(1024).decode()
            print(f'Получено сообщение {data}')
        except:
            pass
    time.sleep(1)