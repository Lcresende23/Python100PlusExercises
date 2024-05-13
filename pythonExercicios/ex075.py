numeros = (int(input('Digite um número:')), int(input('Digite outro número:')),
           int(input('Digite mais um número:')), int(input('Digite o ultimo número:')))
print(f'Você digitou os valores {numeros}')

print(f'O Número 9 apareceu {numeros.count(9)}x')
if 3 in numeros:
    print(f'O numero 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi localizado na tupla.')
print('Os valores pares digitados foram ', end= '')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
