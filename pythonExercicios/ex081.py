#Extraindo dados de uma lista

lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print(f'A lista completa na ordem digitada é: \033[33m{lista}\033[m\n')

print(f'Foram diigitados \033[33m{len(lista)}\033[m números na lista\n')

lista.sort(reverse=True)
print(f'A lista em ordem decrescente ficou \033[33m{lista}\033[m\n')

if 5 in lista:
    print('O valor \033[33m5\033[m apareceu na lista\n')
else:
    print('Não encontramos o valor 5')