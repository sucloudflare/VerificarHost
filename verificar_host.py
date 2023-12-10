# Importa todas as funcionalidades da biblioteca Scapy
from scapy.all import *

def verificar_hosts():
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


def obter_endereco_ip(nome_do_host):
    try:
        # Envia um pacote DNS para obter o endereço IP associado ao nome do host
        resposta = sr1(IP(dst="8.8.8.8") / UDP(sport=RandShort(), dport=53) / DNS(rd=1, qd=DNSQR(qname=nome_do_host)), verbose=0, timeout=2)
        
        # Verifica se a resposta contém informações de IP
        if resposta and resposta.haslayer(IP):
            endereco_ip = resposta[IP].src
            print(f'O endereço IP de {nome_do_host} é {endereco_ip}')
        else:
            print(f'Não foi possível obter o endereço IP para o host {nome_do_host}')
    except Exception as e:
        print(f'Erro ao obter o endereço IP: {str(e)}')

def verificar_hosts():
    while True:
        nome_do_host = input("Digite o nome do host (exemplo: www.google.com): ")

        if not nome_do_host:
            print("\033[91m[!] Nenhum host fornecido. Digite pelo menos um host.\033[97m")
            continue

        # Verifica se o host foi inserido corretamente
        if "." not in nome_do_host:
            print("\033[91m[!] Nome de host inválido. Certifique-se de incluir um domínio válido (exemplo: www.google.com).\033[97m")
            continue

        obter_endereco_ip(nome_do_host)

        novamente = input("Deseja verificar outro host? (s/n): ").lower()
        if novamente != 's':
            break

if __name__ == "__main__":
    verificar_hosts()
