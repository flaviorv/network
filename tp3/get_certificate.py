import socket, ssl, pprint
from datetime import datetime

def get_https_certificate(host, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            certificate = ssock.getpeercert()
    return certificate

def check_certificate(certificate):
    current_date = datetime.now(tz=None)
    expiration_date = datetime.strptime(certificate['notAfter'], "%b %d %H:%M:%S %Y GMT")
    if current_date > expiration_date:
        print(f"Certificate expired on {expiration_date}")
    else:
        print(f"Certificate is valid until {expiration_date}")
 
if __name__ == '__main__':
    host = 'www.example.org'
    print(f"Getting security certificate from {host}...")
    certificate = get_https_certificate(host)
    pprint.pprint(certificate)
    check_certificate(certificate)
