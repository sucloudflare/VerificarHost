# Importa todas as funcionalidades da biblioteca Scapy
from scapy.all import *

def exibir_logo():
    verificarhost_logo = """\033[93m
       ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄██████▄
      ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███
      ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀
     ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███ 
    ▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄
      ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███
      ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███
      ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀
                                             ▀                                                               
    \033[94m[✔] https://github.com/sucloudflare/VerificarHost   [✔]
    \033[94m[✔]            Version 1.1               [✔]
     \033[97m"""

    print(verificarhost_logo)
import socket
import sys

def scan(host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((host, int(port)))
            if code == 0:
                print("[+] {} open".format(port))
            client.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(",")
        else:
            ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]

        scan(host, ports)
    else:
        print("Usage: python portscan.py google.com 22,23,80,443")
