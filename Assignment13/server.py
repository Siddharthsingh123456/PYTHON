
import socket

host = '127.0.0.1'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Server started. Waiting for connection...")

conn, addr = server.accept()
print("Connected by:", addr)

while True:
    message = conn.recv(1024).decode()

    if message.lower() == 'exit':
        print("Client disconnected.")
        break

    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == 'exit':
        break

conn.close()
server.close()
