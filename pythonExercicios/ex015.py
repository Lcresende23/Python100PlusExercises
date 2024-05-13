# Aluguel de carro

dia = int(input('Informe a quantidade de dias em que o veículo ficou alugado: '))
km = float(input('Informe a quantidade de KM rodado com o veículo: '))

total = (dia * 60) + (km * 0.15)

print('\nO total de dias em que o veículo ficou alugado é de {}'.format(dia))
print('A quantidade de KM rodados com o veículo nesse período foi de {}'.format(km))
print('A conta total ficou em R${:.2f}'.format(total))
