# converter metros em centimentros e milimetros

metro = float(input('Quantos metros você deseja converter? \n'))

mili = metro * 1000
centi = metro * 100

print('Você informou um tamanho de {} metro(s)'.format(metro))
print('{} metro(s) tem {} centímetros'.format(metro, centi))
print('{} metro(s) tem {} milimetros'.format(metro, mili))


