import dns.resolver


domain = "example.com"
 
try:
    print("Domain:", domain)
    print(f"A records:", end=" ")
    res = dns.resolver.resolve(domain, 'A')
    for i in res:
        print(i.to_text())
 
    print(f"\nMX records:", end=" ")
    res = dns.resolver.resolve(domain, 'MX')
    for i in res:
        print(f"Prioridade: {i.preference}, Servidor: {i.exchange}")
 
    print(f"\nNS records:", end=" ")
    res = dns.resolver.resolve(domain, 'NS')
    for i in res:
        print(i.to_text())
except Exception as e:
    print(f"ERROR: {e}")
