# Importa todas as funcionalidades da biblioteca Scapy
from scapy.all import *

# Lista de hosts que serão analisados
hosts = ["google.com"]

# Constrói um pacote IP com um segmento TCP para realizar a varredura de portas
pacote = IP(dst=hosts)/TCP(dport=(1,500), flags="S")

# Envia o pacote construído e aguarda por respostas, com um timeout de 1 segundo
respondidos, nao_respondidos = sr(pacote, timeout=1)

# Itera sobre as respostas recebidas
for n in range(len(respondidos)):
    # Imprime o endereço IP de destino e a porta de destino para cada resposta
    print("{} -> {}".format(respondidos[n][0][IP].dst, respondidos[n][0][TCP].dport))
