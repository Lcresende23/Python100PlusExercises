# Calcular área com parâmetro e função

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}X{c} é de {a}m².')


l = float(input('Largura do terreno: '))
c = float(input('Comprimento do terrreno: '))
area(l, c)

