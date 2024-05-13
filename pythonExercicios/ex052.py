num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end='')
    else:
        print('\33[31m', end='')
    print('{}'.format(c), end=' ')
print('\no número {} foi divisivel por {} números.'.format(num, tot), end=' ')
if tot == 2:
    print('Então, ele é PRIMO.')
else:
    print('Então, ele não é PRIMO.')

