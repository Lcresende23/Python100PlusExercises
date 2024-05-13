# Calculando IMC

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso/(altura **2)

if imc < 18.5:
    print('Seu IMC é de {:.1f} e você está abaixo do peso ideal.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f} e você está no peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f} e você está acima do peso ideal.'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é de {:.1f} e você está com obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.1f} e você tem obesidade morbida.'.format(imc))