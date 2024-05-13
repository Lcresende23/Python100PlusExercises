#Alistamento militar
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))

hoje = date.today().year

idade = hoje - ano


if idade == 18:
    print('Você tem {} anos e está na hora de se alistar! '.format(idade))

elif idade < 18:
    saldo = 18 - idade
    print('Você tem {} anos. Ainda irá chegar sua vez de se alistar daqui {} anos'.format(idade, saldo))
    alistamento = hoje + saldo
    print('Você irá se alistar no ano {}'.format(alistamento))


elif idade > 18:
    saldo = idade - 18
    print('Você tem {} anos e deveria ter se alistado há {} anos atrás'.format(idade, saldo))
    alistamento = hoje - saldo
    print('Você deveria ter se alistado no ano de {}'.format(alistamento))