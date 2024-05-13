#Lista com Pares e ímpares

numeros = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print('_' * 30)

numeros[0].sort()
numeros[1].sort( )
print(f'Os valores PARES digitados foram {numeros[0]}')
print(f'Os valores ÍMPARES digitados foram {numeros[1]}')


