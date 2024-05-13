tot = MaisMil = cont = 0
MaisBarato = 0
NomeBarato = ' '

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    cont += 1
    tot += preco

    if preco > 1000:
        MaisMil += 1

    if cont == 1:
        MaisBarato = preco
        NomeBarato = nome
    else:
        if preco < MaisBarato:
            MaisBarato = preco
            NomeBarato = nome

    r = ' '
    while r not in 'SN':
        r = str(input('Deseja cadastrar mais? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print(f'O total gasto na compra foi: {tot:.2f}')
print(f'{MaisMil} produtos custaram mais de R$1.000,00')
print(f'O produto mais barato: {NomeBarato} que custou {MaisBarato}')
