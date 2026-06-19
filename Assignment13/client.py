
import socket

host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print("Connected to server.")

while True:
    message = input("Client: ")
    client.send(message.encode())

    if message.lower() == 'exit':
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == 'exit':
        break

client.close()
