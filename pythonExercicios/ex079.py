#valores unicos em uma lista

lista = []
num = 0

while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado!')

    else:
        print('Valor repetido! Não vou adicionar')

    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break


lista.sort()
print(f'A lista em ordem cresente é {lista}')