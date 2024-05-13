# Jogo de dados em Python

from random import randint
from time import sleep
from operator import itemgetter
maior = menor = 0
jogador = {'Jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('Números sorteados no dado: ')
for k, v in jogador.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('\nRanking dos vencedores:  \n')
for i, v in enumerate(ranking):
    print(f'{i+1}ºLugar: {v[0]} com {v[1]}')
    sleep(1)






