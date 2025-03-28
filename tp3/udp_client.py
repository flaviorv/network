if __name__ == "__main__":
    import socket

    SERVER_HOST = "flavioshost"
    SERVER_PORT = 1500

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello Server"
    print(f"Sending to server ({SERVER_HOST}:{SERVER_PORT}):", message)
    client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
    data, _ = client_socket.recvfrom(1024)
    print(f"Server sent a message: {data.decode()}")
    client_socket.close()
