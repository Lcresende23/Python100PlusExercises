#SOMA DE NUMEROS IMPARES
s = 0
cont = 0
for c in range (1, 7):
    n = int(input('Digite um número inteiro'))
    if n % 2 == 0:
        s += n
        cont += 1

print('A soma de todos os {} VALORES PARES DIGITADOS É: {}'.format(cont, s))