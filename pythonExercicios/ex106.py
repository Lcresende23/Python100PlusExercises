# Interactive Help
from time import sleep

c = ('\033[m', '\033[0:30:41m', '\033[0;30;44m', '\033[0;30;45m')  # 1-  vermelho   # 0 - Sem cores

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[3], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=1):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('ANÁLISADOR DE FUNÇÃO', 1)
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)


