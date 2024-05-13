# CUSTO DA VIAGEN

distancia = float(input('Qual a distancia da viagem em Km? Informe aqui: '))

print('Você irá viajar uma distancia de {}Km'.format(distancia))

if distancia <=200:
    preco = distancia * 0.50

else:
    preco = distancia * 0.45
print('A sua viagem irá custar R${:.2f}'.format(preco))

