#Fatorial

num = int(input('Digite o número que deseja fatorar: '))
c = num
tot = 1
print('Calculando fatorial de {}! = '.format(num),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    tot *= c
    c -= 1


print('O fatorial de {} é {}'.format(num, tot))
