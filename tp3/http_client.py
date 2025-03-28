import socket

HOST, PORT = 'flavioshost', 1600
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
header = "GET / HTTP/1.1\nHost: flavioshost:1600\nAccept: text/html\nConnection: close\n\n"
client.connect((HOST, PORT))
client.sendall(header.encode())
res =b''
while True:
    data = client.recv(1024)
    if not data:
        break
    res+=data

print(res.decode('utf-8'))
client.close()