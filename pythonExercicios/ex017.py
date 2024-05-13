#Calcular o comprimento da hipostenusa
import math

a = float(input('Digite o valor do cateto A: '))
b = float(input('Digite o valor do cateto B: '))
h = math.hypot(a, b)




print('Você informou que o cateto A é {}, o cateto B é {}, dessa maneira a hipotenusa será {:.2f}'.format(a, b, h))
