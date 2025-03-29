import socket, ssl

SERVER, PORT = "flavioshost", 4444

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations("certificate.pem")
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure = context.wrap_socket(client, server_hostname=SERVER)

secure.connect((SERVER, PORT))
print(f'Connected to {SERVER}')

message = "Hello server TLS"
secure.sendall(message.encode())

data = secure.recv(1024)
print(f'Received from server: {data.decode()}')
secure.close()