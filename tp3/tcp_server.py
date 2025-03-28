def start_server(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening in {HOST}:{PORT}")
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection established in {addr}")
                msg = "Hello TCP client"
                print(f"Sending to {addr}: {msg}")
                conn.sendall(msg.encode())
                data = conn.recv(1024)
                print(f"Client {addr} sent a message: {data.decode()}")

if __name__ == "__main__":
    import socket

    HOST = 'flavioshost'
    PORT = 1600
    start_server(HOST, PORT)
