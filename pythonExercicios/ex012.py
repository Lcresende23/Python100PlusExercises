#desconto de 5% em algum produto

valor = float(input('Qual o valor do produto que deseja comprar? '))

desc = valor - (valor * 5/100)

print('O valor do produto é de {}. Com desconto de 5%, ficará por {:.2f}'.format(valor, desc))

