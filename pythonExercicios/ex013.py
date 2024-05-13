# calcular o salário com 15% de aumento

sal = float(input('Digite o salário que deseja adicionar o aumento: '))

novo = sal + (sal*15/100)

print('O sálario antigo do funcionário era de {} e com o aumento de 15% foi para {:.2f}'.format(sal, novo))
