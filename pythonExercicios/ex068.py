#PAR OU IMPAR
from random import randint
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('PAR OU IMPAR? [P/I]?')).strip().upper()[0]
    print(f'Jogador Jogou {jogador} e o computador jogou {comp} e a soma é {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
print(f'GAME OVER! Você venceu {v}x seguidas! ')







