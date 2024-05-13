from random import randint
from time import sleep

palpite = 0
acertou = False
print('-=-'*10)
print('\t\033[31mJogo da adivinhação\033[m')
print('-=-'*10)
comp = randint(0, 10)
print('Acabei de pensar em um número, será que voce consegue adivinhar?')

while not acertou:
    jogador = int(input('Qual seu palpite: '))
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais... Tente novamente')
        elif jogador > comp:
            print('Menos... Tente novamente')

print('\033[33mParabéns, conseguiu adivinhar o número com {} palpites\033[m'.format(palpite))