# Funções com modularização formatado

import moeda

num = float(input('Digite um valor R$: '))
print(f'O valor digitado foi {moeda.moeda(num)}')
print(f'O valor com acrescimo de 10% foi de {moeda.aumentar(num, 10, True)}')
print(f'O valor com desconto de 13% foi de {moeda.diminuir(num, 13, True )}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
