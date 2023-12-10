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


Abra o arquivo verificar_host.py em um editor de texto.

   Modifique a lista hosts para incluir os hosts que você deseja analisar. Exemplo:

   python

hosts = ["google.com", "example.com"]

Execute o script:

bash

    python3 verificar_host.py

  O script enviará pacotes para as portas especificadas nos hosts e imprimirá as portas abertas.

Aviso

Este script deve ser usado apenas para fins educacionais ou em ambientes nos quais você tenha permissão para realizar varreduras de portas. A execução de varreduras sem autorização pode violar políticas de segurança e leis.
Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.

MIT License

Copyright (c) 2023 Edson Bruno


h1>Port Scanner</h1>

<p>Um script simples de varredura de portas em Python que verifica se determinadas portas em um host estão abertas.</p>

<h2>Requisitos</h2>

<ul>
    <li>Python 3.x</li>
</ul>

<h2>Uso</h2>

<p>Execute o script da seguinte maneira:</p>

<pre>
<code>python portscan.py &lt;host&gt; &lt;portas&gt;</code>
</pre>

<p>Se nenhum argumento for fornecido para as portas, as seguintes portas serão verificadas por padrão: 21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135.</p>

<p>Exemplo:</p>

<pre>
<code>python portscan.py google.com 80,443,8080</code>
</pre>

<h2>Contribuindo</h2>

<p>Sinta-se à vontade para contribuir com melhorias, correções de bugs ou adição de recursos. Abra uma issue para discutir grandes alterações antes de enviar um pull request.</p>

<h2>Aviso</h2>

<p>Este script é fornecido apenas para fins educacionais. Não use este script para varredura de portas em sistemas que você não possui ou não tem permissão para testar.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a <a href="LICENSE">MIT License</a>.</p>


