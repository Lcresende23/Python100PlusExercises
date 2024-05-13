# Funções com modularização

import moeda

num = float(input('Digite um valor R$: '))
print(f'O valor digitado foi R${num}')
print(f'O valor com acrescimo de 10% foi de R${moeda.aumentar(num, 10)}')
print(f'O valor com desconto de 13% foi de R${moeda.diminuir(num, 13)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')