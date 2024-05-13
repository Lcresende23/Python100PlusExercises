#palpites mega sen
from random import randint
from time import sleep
lista = list()
totjogos = list()
tot = 1
print('_' * 30)
print(f'   {"MEGA SENA":^25}   ')
print('_' * 30)
jogos = int(input('Quantos jogos deseja fazer? '))
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    totjogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteando {jogos} jogos')

for c, n in enumerate(totjogos):
    print(f'Jogo {c+1}: {n}')
    sleep(1)
print('BOA SORTE!')


