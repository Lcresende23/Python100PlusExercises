#TABUADA 3.0
total = 0
while True:
    n = int(input('Qual tabuada deseja mostrar? '))
    if n < 0:
        break

    for c in range (1, 11):
        total = n * c
        print(f'{n} x {c} = {total}')

print('Programa finalizado!')

