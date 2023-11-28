# VerificarHost

<img src='https://egx9daq4q4y.exactdn.com/wp-content/uploads/2020/12/hacking.jpg?strip=all&lossy=1&w=900&ssl=1'>

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


Abra o arquivo verificar_host.py em um editor de texto.

   Modifique a lista hosts para incluir os hosts que você deseja analisar. Exemplo:

   python

hosts = ["google.com", "example.com"]

Execute o script:

bash

    python verificar_host.py

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




