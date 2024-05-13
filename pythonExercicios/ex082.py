#dividindo valores em várias listas

lista = []
listaPar = []
listaImpar = []

while True:
    lista.append(int(input('Digite um número: ')))

    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print(f'A lista completa é \033[33m{lista}\033[m\n')

for c, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    else:
        listaImpar.append(v)

print(f'A lista contendo os valores PARES é \033[33m{listaPar}\033[m\n')
print(f'A lista contendo os valores IMPARES é \033[33m{listaImpar}\033[m')
