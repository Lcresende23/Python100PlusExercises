#Natação

from datetime import date

ano = int(input('Digite o ano de nascimento: '))

atual = date.today().year

idade = atual - ano

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('A idade é {} anos e esta na categoria MIRIN.'.format(idade))
elif idade <= 14:
    print('A idade é {} anos e esta na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('A idade é {} anos e esta na categoria JUNIOR.'.format(idade))
elif idade <= 25:
    print('A idade é {} anos e esta na categoria SENIOR.'.format(idade))
elif idade > 20:
    print('A idade é {} e esta na categoria MASTER'.format(idade))

