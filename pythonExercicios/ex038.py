#Comparador de números

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print('O primeiro valor digitado foi {} e ele é maior que o segundo valor digitado!'.format(n1))
elif n2 > n1:
    print('O segundo valor digitado foi {} e ele é maior que o primeiro digitado!'.format(n2))
elif n1 == n2:
    print('Não existe valor maior pois os dois são iguais!')
