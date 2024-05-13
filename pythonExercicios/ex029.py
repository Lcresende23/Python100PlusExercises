# RADAR ELETRONICO

print('Radar Eletrônico')

velocidade = float(input('Digite a velocidade em que o carro passou: '))

#multa = (velocidade - 80) * 7

if velocidade >80:
    print('Você ultrapassou o limite de 80Km/h e será multado no valor de R${:.2f} '.format((velocidade - 80)*7))
else:
    print('Passou no limite de velocidade permitido.')

