import socket
import threading

host = "127.0.0.1"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []


def send_to_all(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            send_to_all(message)
        except:
            clients.remove(client)
            client.close()
            break


print("Server is running...")

while True:
    client, address = server.accept()
    print("Connected with", address)

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
  
