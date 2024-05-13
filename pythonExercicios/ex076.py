lista = ('Leite', 3.50, 'Pão', 0.60, 'Café', 11.40, 'Açucar', 3.10, 'Sal', 2.75, 'Arroz', 35.00, 'Picanha', 130.00)
print('_'*38)
print(f'{"Lista de produtos e compras":^40}')
print('_'*38)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}R$ {lista[pos+1]:.2f}')
print('_'*38)
