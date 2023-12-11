# VerificarHost

<img src='https://egx9daq4q4y.exactdn.com/wp-content/uploads/2020/12/hacking.jpg?strip=all&lossy=1&w=900&ssl=1'>

# Scanner de Portas em Python usando verificar_host

Este script Python utiliza a biblioteca Scapy para realizar uma varredura de portas em um ou mais hosts. A varredura de portas é uma técnica comumente usada em testes de penetração para identificar quais portas em um host estão abertas e podem ser vulneráveis.

## Requisitos

- Python 3.x
- verificar_host

Você pode instalar a biblioteca verificar_host usando o seguinte comando:

```bash
   pip3 install verificar_host
```
Caso não pegue, versão alternativa: 
```
   pip3 install --upgrade scapy
   pip3 install scapy
```
Uso

<h1>Port Scanner</h1>

<p>Um script simples de varredura de portas em Python que verifica se determinadas portas em um host estão abertas.</p>

<p>Execute o script da seguinte maneira:</p>

<pre>
<code>
cd VerificarHost
sudo python3 verificar_host.py -h
</code>
</pre>

<p>Se nenhum argumento for fornecido para as portas, as seguintes portas serão verificadas por padrão: 21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135.</p>

<p>Exemplo:
</pre>
<pre>
sudo python3 verificar_host.py google.com 80,443,8080</code>
</pre>

<h2>Contribuindo</h2>

<p>Sinta-se à vontade para contribuir com melhorias, correções de bugs ou adição de recursos. Abra uma issue para discutir grandes alterações antes de enviar um pull request.</p>

<h2>Aviso</h2>

<p>Este script é fornecido apenas para fins educacionais. Não use este script para varredura de portas em sistemas que você não possui ou não tem permissão para testar.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a <a href="LICENSE">MIT License</a>.</p>

<h2>IMG</h2>

<img src='./a.png'>


