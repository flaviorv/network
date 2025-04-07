from scapy.all import *

def processing(packet):
      if packet.haslayer(UDP) and Raw in packet:
        signature = "[INTERCEPTADO]"
        msg = packet[Raw].load.decode()
        if signature not in msg:
            print(f"[+] Captured: {msg}")
            new_message = (signature+msg).encode()
            corrupted_packet = IP(src=packet[IP].src, dst=packet[IP].dst)/UDP(sport=packet[UDP].sport, dport=packet[UDP].dport)/Raw(load=new_message)
            send(corrupted_packet, verbose=0)
            print("[*] Corrupted packet sent.")

def sniffing(interface, port):
    filtro = f"udp and port {port}"
    print(f"[*] Listening inteface '{interface}' on port {port}...")
    
    sniff(
        iface=interface,
        filter=filtro,
        prn=processing,
        store=0
    )

if __name__ == "__main__":
    sniffing("lo", 9000)
