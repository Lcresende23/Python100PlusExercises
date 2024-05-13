#Aprovando empréstimo

print('Cotação de empréstimo')
print('-=-'*12)

casa = float(input('Digite o valor do imóvel que deseja comprar: '))
anos = int(input('Digite em quantos anos deseja pagar: '))
salario = float(input('Digite o valor do seu salário: '))

divisao = casa / (anos * 12)
minimo = salario * 30/100

print('O valor da casa é de R${:.2f} que dividido em {} anos, as parcelas serão de {:.2f}'.format(casa, anos, divisao))

if divisao <= minimo:
    print('Tudo certo, o valor da parcela ficará em {:.2f} e você pode pegar '
          'seu emprestimo nessas condições!'.format(divisao))

else:
    print('Infelizmente o valor de sua parcela excede 30% do seu salário')