def start_server(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening in {HOST}:{PORT}")
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection established in {addr}")
                send_file(conn, "image.png")
                receive_file(conn, "received_from_client.png")

def send_file(sock, filename):
    filesize = os.path.getsize(filename)
    sock.sendall(struct.pack("<Q", filesize))
    with open(filename, "rb") as f:
        while read_bytes := f.read(1024):
            sock.sendall(read_bytes)

def receive_file(sock, filename):
    filesize = receive_file_size(sock)
    with open(filename, "wb") as f:
        received_bytes = 0
        while received_bytes < filesize:
            chunk = sock.recv(1024)
            if chunk:
                f.write(chunk)
            received_bytes += len(chunk)

def receive_file_size(sock):
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        chunk = sock.recv(expected_bytes - received_bytes)
        stream += chunk 
        received_bytes += len(chunk)
        filesize = struct.unpack(fmt, stream)[0]
    return filesize

if __name__ == "__main__":
    import socket, struct, os
    HOST = 'flavioshost'
    PORT = 1600
    start_server(HOST, PORT)
