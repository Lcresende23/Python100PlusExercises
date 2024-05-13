# unindo dicionários e listas

ficha = dict()
cadastro = list()
soma = 0

while True:
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if ficha['sexo'] in 'MF':
            break
        print('Erro! Digite = M OU F ')
    ficha['idade'] = int((input('Idade: ')))
    soma += ficha['idade']
    cadastro.append(ficha.copy())

    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continaur? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break

print('_' * 30)
print(f'Ao todo, foram cadastradas {len(cadastro)} pessoas')
media = soma / len(cadastro)
print(f'A média de idade é de {media:5.2f}')
print('As mulheres cadastradas foram: ', end=' ')
for p in cadastro:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in cadastro:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('\nFIM')




