#Lista composta e análise de dados
dados = list()
pessoas = list()
MaisPesados = list()
MaisLeves = list()

maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print(f'O total de pessoas cadastradas foi de {len(pessoas)} pessoas')

print(f'O maior peso foi {maior}KG e é do', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]...', end=' ')
print(f'\nO menor peso foi {menor}KG que é do', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]...', end=' ')