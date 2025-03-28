if __name__ == "__main__":
    import socket

    HOST = "flavioshost"
    PORT = 1500

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"UDP server is listening on port {PORT}...")
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Client {addr} sent a message: {data.decode()}")
        server_socket.sendto(b"ack", addr)

