# Cadastro de trabalhador

from datetime import date
hoje = date.today().year
ficha = dict()

ficha['nome'] = str(input('Nome: '))
dn = int(input('Ano de nascimento: '))

idade = hoje - dn

ficha['nascimento'] = idade
ficha['carteira'] = int(input('Carteira de trabalho (0 se não possuir): '))
if ficha['carteira'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário R$:  '))
    ficha['aposentadoria'] = ficha['nascimento'] + ((ficha['contratação'] + 35) - hoje)
print('_' * 30)
print(ficha)
print('_' * 30)
print(f'O cidadão se chama {ficha["nome"]}')
print(f'Sua idade é {ficha["nascimento"]} anos')
if ficha['carteira'] == 0:
    print('Ainda não possui carteira de trabalho!')
    print('_' * 30)

for k, v in ficha.items():
    print(f' - {k} tem o valor {v}')

'''else: 
    print('_' * 30)
    print(f'Carteira de trabalho: {ficha["carteira"]}')
    print(f'O {ficha["nome"]} foi contratado em {ficha["contratação"]}')
    print(f'Atualmente o {ficha["nome"]} possui o salário de R${ficha["salario"]}')
    print(f'Irá se aposentar com {ficha["aposentadoria"]} anos')
    print('_' * 30)'''






