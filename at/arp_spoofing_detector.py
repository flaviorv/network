from scapy.all import ARP, sniff

arp = {}
def check(pkt):
    if pkt.haslayer(ARP):
        print(f"Itercepted: {pkt.summary()}")
        if pkt[ARP].op == 2:
            ip = pkt[ARP].psrc
            mac = pkt[ARP].hwsrc
            if ip in arp:
                if arp[ip] != mac:
                    print(f"Warning: Possible ARP Spoofing detected for IP {ip}!")
                    print(f"Previous MAC: {arp[ip]}, current MAC: {mac}")
            else:
                arp[ip] = mac
    
sniff(iface="wlo1", filter="arp", prn=check, store=0)
