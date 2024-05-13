# Funções para votação
def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        print(f'Você tem {idade} anos e não pode votar!')
    elif idade < 18 or idade >= 65:
        print(f'Você tem {idade} anos e o voto é OPCIONAL!')
    elif idade >= 18:
        print(f'Você tem {idade} anos e o voto é OBRIGATÓRIO!')


num = int(input('Digite o ano do seu nascimento: '))
voto(num)