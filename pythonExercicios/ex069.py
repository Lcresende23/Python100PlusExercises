#ler idade e sexo de varias pessoas
from datetime import date

hoje = date.today().year

maior18 = idade = masc = fem = 0
while True:
    print('_' * 20)
    print('\033[33mCADASTRO DE PESSOAS\033[m')
    print('_' * 20)

    ano = int(input('Digite seu ano de nascimento: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

    idade = hoje - ano

    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1

    r = ' '
    while r not in 'SN':
        r = str(input('\n\033[31mDeseja cadastrar mais alguém? [S/N]:\033[m')).strip().upper()[0]
    if r == 'N':
        break

print(f'Foram cadastradas {maior18} pessoas maiores de 18 anos')
print(f'\nForam cadastrados {masc} homens')
print(f'\nForam cadastradas {fem} mulheres com menos de 20 anos')