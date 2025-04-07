import socket

HOST = '127.0.0.1'
PORT = 9000
MENSAGEM = "Original message UDP"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(MENSAGEM.encode(), (HOST, PORT))
    print("[+] Message sent!")
