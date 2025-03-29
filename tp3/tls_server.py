import socket, ssl

HOST, PORT = "flavioshost", 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="certificate.pem", keyfile="pk.pem")
print(f"Server is running at {HOST}:{PORT}")

while True:
    connection, address = server.accept()
    secure = context.wrap_socket(connection, server_side=True)
    print(f"{address} connected")

    data = secure.recv(1024)
    if data:
        print(f"Received from client: {data.decode()}")
        secure.sendall(data)
        secure.close()
