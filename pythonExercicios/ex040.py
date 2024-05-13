#Média escolar

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digita a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi {} e você esta reprovado!'.format(media))

elif media >= 5 and media < 7:
    print('Sua nota foi {} e você esta de recuperação!'.format(media))

elif media >= 7:
    print('Parabéns! Sua nota foi {} e você está aprovado!'.format(media))

