# Prestar atenção:
o programa está atualmente farejando a primeira interface que pode ser encontrada (principalmente eth0). Você pode especificar uma interface específica nas configurações do scapy ou adicionando "iface=<INTERFACE>" nos locais que o scapy fareja ou envia pacotes!

# Autor:
Sp4rkN3r0
# Licença:
MIT

# SilentBackDoor
um backdoor que não captura uma porta do pc, assim ninguém verá que existe um backdoor.

# Uso
a principal operação do backdoor é usar scapy e sniff para pacotes sem capturar a porta, os comandos estão sendo separados dos argumentos usando : e os argumentos estão sendo passados ​​como string.
por exemplo, atualmente temos o comando is_alive para verificar se o backdoor está ativo.
para executar o comando, envie do PC invasor o comando:
Está vivo:
preste atenção, mesmo que não tenhamos parâmetros, temos que adicionar o ":" e a função tem que obter argumentos porque está sendo mantida em um dict para facilitar a adição de funções.
