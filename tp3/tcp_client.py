def start_client(SERVER_HOST, SERVER_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        data = client_socket.recv(1024)
        print(f"Server {SERVER_HOST}:{SERVER_PORT} sent: {data.decode()}")
        msg = "Hello TCP server"
        print(f"Sending to server({SERVER_HOST}:{SERVER_PORT}):", msg)
        client_socket.sendto(msg.encode(), (SERVER_HOST, SERVER_PORT))

if __name__ == "__main__":
    import socket

    SERVER_HOST = 'flavioshost'
    SERVER_PORT = 1600
    start_client(SERVER_HOST, SERVER_PORT)