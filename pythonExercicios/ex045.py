#JOKEMPOOOOO
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'tesoura')
comp = randint(0, 2)

print('======Pedra, papel e tesoura ======')
print('Escolha: \n0 - Pedra\n1 - Papel\n2 - Tesoura')

jogador = int(input('Você escolhe Pedra, Papel ou tesoura?'))
print('_'*25)
print('JOOO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[comp]))
print('_'*25)

if comp == 0:
    if jogador == 0:
        print('Empate!')

    elif jogador == 1:
        print('Jogador ganhou!')

    elif jogador == 2:
        print('Computador ganhou!')

    else:
        print('Jogada inválida!')
if comp == 1:
    if jogador == 0:
        print('Computador venceu!')

    elif jogador == 1:
        print('Empate!')

    elif jogador == 2:
        print('Jogador venceu!')

    else:
        print('Jogada Inválida')

if comp == 2:
    if jogador == 0:
        print('Jogador venceu!')

    elif jogador == 1:
        print('Computador venceu!')

    elif jogador == 2:
        print('Empate!')

    else:
        print('Jogada inválida')