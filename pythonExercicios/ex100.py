# Função pra sortear e somar
from random import randint
from time import sleep


def sorteia(*valores):
    print('Os valores sorteados foram ', end='')
    for v in valores:
        print(f'{v} ', end='', flush=False)
        sleep(0.5)
        sorteados.append(v)
    print()


def somaPar(num):
    s = 0
    for v in num:
        if v % 2 == 0:
            s += v
    print(f'A soma dos Valores pares de {num} é {s}')


sorteados = list()

sorteia(randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10),
        randint(1, 10))

somaPar(sorteados)

