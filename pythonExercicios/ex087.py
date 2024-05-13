#análise dos dados da matriz

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somacoluna = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
        if matriz[l][c] % 2 ==0:
            par += matriz[l][c]
    print()

print('_'* 40)
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma da Terceira coluna é {somacoluna} ')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda coluna é {maior}')
