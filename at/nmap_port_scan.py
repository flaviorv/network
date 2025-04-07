import subprocess
import sys
import asyncio

async def run_nmap_async(ip):
    process = await asyncio.create_subprocess_exec(
        'nmap', '-sS', '-sV', ip,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if process.returncode == 0:
        print(f"[{ip}] result:\n{stdout.decode()}")
    else:
        print(f"[{ip}] error:\n{stderr.decode()}")

def run_nmap_sync(ip):
    result = subprocess.run(
        ['nmap', '-sS', '-sV', ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode == 0:
        print(f"[{ip}] result:\n{result.stdout}")
    else:
        print(f"[{ip}] error:\n{result.stderr}")

async def main_async(ips):
    tasks = [run_nmap_async(ip) for ip in ips]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 nmap_port_scan.py [sync|async] ip1 [ip2 ip3 ...]")
        sys.exit(1)
    mode = sys.argv[1]
    ips = sys.argv[2:]
    if mode == 'sync':
        for ip in ips:
            run_nmap_sync(ip)
    elif mode == 'async':
        asyncio.run(main_async(ips))
    else:
        print("Invalid input. Use 'sync' or 'async'.")
