import requests
import sys
from urllib.parse import urljoin

def load_wordlist(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def fuzz(base_url, wordlist):
    print(f"Iniciando fuzz em: {base_url}")
    found = []
    for path in wordlist:
        url = urljoin(base_url, path)
        try:
            response = requests.get(url, timeout=3)
            status = response.status_code
            if status in [200, 301, 302, 403]:
                print(f"[{status}] Encontrado: {url}")
                found.append((url, status))
            else:
                print(f"[{status}] {url}")
        except requests.RequestException as e:
            print(f"[ERRO] {url} -> {e}")
    return found

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 fuzzer.py <url_base> <wordlist.txt>")
        sys.exit(1)
    base_url = sys.argv[1]
    wordlist_file = sys.argv[2]
    wordlist = load_wordlist(wordlist_file)
    results = fuzz(base_url, wordlist)
    print("\nCaminhos encontrados:")
    for url, status in results:
        print(f"{url} - Status {status}")
