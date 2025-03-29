def start_client(SERVER_HOST, SERVER_PORT, filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")
    receive_file(client_socket, filename)
    send_file(client_socket, "image.png")
    client_socket.close()

def receive_file(sock, filename):
    filesize = receive_file_size(sock)
    with open(filename, "wb") as f:
        received_bytes = 0
        while received_bytes < filesize:
            chunk = sock.recv(1024)
            if chunk:
                f.write(chunk)
            received_bytes += len(chunk)
        print(f"The file {filename} has been downloaded")

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

def send_file(sock, filename):
    filesize = os.path.getsize(filename)
    sock.sendall(struct.pack("<Q", filesize))
    with open(filename, "rb") as f:
        while read_bytes := f.read(1024):
            sock.sendall(read_bytes)
        print(f"The file {filename} has been uploaded")

if __name__ == "__main__":
    import socket, struct, os

    SERVER_HOST = 'flavioshost'
    SERVER_PORT = 1600
    start_client(SERVER_HOST, SERVER_PORT, "received_from_server.png")
    