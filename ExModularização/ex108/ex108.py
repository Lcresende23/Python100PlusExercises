# Funções com modularização formatado

import moeda



import moeda

num = float(input('Digite um valor R$: '))
print(f'O valor digitado foi {moeda.moeda(num)}')
print(f'O valor com acrescimo de 10% foi de {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'O valor com desconto de 13% foi de {moeda.moeda(moeda.diminuir(num, 13))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
