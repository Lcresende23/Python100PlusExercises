#ler 5 valores e por na lista

lista = []
maior = menor = 0
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para o indice {v}:  ')))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]

print(f'\nVocê criou a lista:  {lista}\n')

print(f'O maior valor digitado foi o \033[33m{maior}\033[m e esta nas posições ', end='')
for c, v in enumerate(lista):
    if lista[c] == maior:
        print(f'{c}...', end='')

print(f'\nO menor valor digitado foi o \033[33m{menor}\033[m e esta nas posições ', end='')
for c, v in enumerate(lista):
    if lista[c] == menor:
        print(f'{c}...', end='')