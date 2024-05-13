#SOMANDO IMPARES MULTIPLOS DE 3
from time import sleep
s = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c

print(' A soma de todos os {} valores ímpares multiplos de 3 é {}'.format(cont, s))

