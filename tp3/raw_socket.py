import socket

raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
raw_socket.bind(("flavioshost", 0))

print("Intercepting raw data...")

while True:
    packet, addr = raw_socket.recvfrom(65565)
    print(f"Received from {addr}")
    print(f"Data: {packet}")
