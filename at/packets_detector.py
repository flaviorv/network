from scapy.all import sniff, IP, TCP, UDP

def show_packages(packet):
    print("\n--- Detected packet ---")
    if IP in packet:
        ori = packet[IP].src
        dest = packet[IP].dst
        print(f"From: {ori} -> To: {dest}")
        if TCP in packet:
            print(f"Protocol: TCP | Origin: {packet[TCP].sport}, Destination: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"Protocol: UDP | Origin: {packet[UDP].sport}, Destination: {packet[UDP].dport}")
        else:
            print("Not TCP, not UDP ")
    else:
        print("No IP")

def capture(interface="wlo1", amount=10):
    print(f"[*] Capturing {amount} packets on interface '{interface}'...")
    sniff(iface=interface, prn=show_packages, count=amount)

if __name__ == "__main__":
    capture()
