# Dicionário em Python

ficha = dict()
media = 0

ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}:  '))

if ficha['media'] >= 7:
    print(f'o nome é {ficha["nome"]}')
    print(f'Sua média ficou em {ficha["media"]}')
    print('E sua situação é: APROVADO!')
else:
    print(f'o nome é {ficha["nome"]}')
    print(f'Sua média ficou em {ficha["media"]}')
    print('Sua situação é: REPROVADO!')



