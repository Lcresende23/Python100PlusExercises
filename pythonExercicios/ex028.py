#jogo da adivinhação
from random import randint
from time import sleep

print('\033[2;33mJOGO DA ADIVINHAÇÃO\033[m')
sleep(4)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5...')
print('Consegue adivinhar o número que eu pensei?')
print('-=-'*20)


jogador = int(input(' Digite um número entre 0 e 5: '))
print('Processando...')
sleep(3)

comp = randint(0, 5) # faz o computador "PENSAR"
print('Pensei no número... {}'.format(comp))

if jogador == comp:
    print('Parabens, acertou o número!!')
else:
    print('Errou! Eu pensei no número {}'.format(comp))
