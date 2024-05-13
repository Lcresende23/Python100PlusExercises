# AUMENTO DE SALARIO

sal = float(input('Digite o valor do salário que será atualizado: '))

if sal > 1250:
    aumento = sal + (sal * 10 / 100)
else:
    aumento = sal + (sal * 15 / 100)
print('Seu salário é de R${:.2f} e com o aumento passará para R${:.2f}'.format(sal, aumento))