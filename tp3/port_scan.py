import socket

ips = ["127.0.0.1", "127.0.0.53", "127.0.0.54"]
ports = [22, 80, 8080, 53, 67, 443, 3000, 12345, 631]

for ip in ips:
    for port in ports:       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = s.connect_ex((ip, port))
        print(f"{ip}:{port} status: {result}")
        s.close()
