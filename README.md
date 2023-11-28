# VerificarHost

# Scanner de Portas em Python usando verificar_host

Este script Python utiliza a biblioteca Scapy para realizar uma varredura de portas em um ou mais hosts. A varredura de portas é uma técnica comumente usada em testes de penetração para identificar quais portas em um host estão abertas e podem ser vulneráveis.

## Requisitos

- Python 3.x
- verificar_host

Você pode instalar a biblioteca verificar_host usando o seguinte comando:

```bash
   pip install verificar_host
```

Uso


Abra o arquivo port_scanner.py em um editor de texto.

   Modifique a lista hosts para incluir os hosts que você deseja analisar. Exemplo:

   python

hosts = ["google.com", "example.com"]

Execute o script:

bash

    python port_scanner.py

  O script enviará pacotes para as portas especificadas nos hosts e imprimirá as portas abertas.

Aviso

Este script deve ser usado apenas para fins educacionais ou em ambientes nos quais você tenha permissão para realizar varreduras de portas. A execução de varreduras sem autorização pode violar políticas de segurança e leis.
Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.

lua


MIT License

Copyright (c) 2023 Edson Bruno

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


