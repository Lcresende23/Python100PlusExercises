somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for c in range(1, 5):
    print('---------{}ª PESSOA-----------'.format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo: [M/F] '))
    print('-=-'*10)

    somaidade += idade
    if idade == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totalmulher20 += 1
media = somaidade / 4
print('\033[33mA média de idade das pessoas é {:.0f} anos'.format(media))
print('\033[33mO homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('\033[33mA quantidade de mulheres acima de 20 anos é {}'.format(totalmulher20))
