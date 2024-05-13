# Função contador
from time import sleep


def contador(i, f, p):
      print('_' * 30)
      print(f'Contagem de {i} até {f} de {p} em {p}')
      print('_' * 30)


      if i < f:
          cont = 1
          while cont <= f:
              print(f'{cont} ', end='', flush=False)
              sleep(0.5)
              cont += p
          print('FIM!')
      else:
          cont = i
          while cont >= f:
              print(f'{cont} ', end='', flush=False)
              sleep(0.5)
              cont -= p
          print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez!')
i = int(input('Digite o número de inicio: '))
f = int(input('Digite o número que irá finalizar: '))
p = int(input('Digite de quanto em quanto irá pular: '))
contador(i, f, p)


