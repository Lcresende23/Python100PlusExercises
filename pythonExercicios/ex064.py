cont = total = num = 0
num = int(input('Digite um número [999 para encerrar]: '))
while num != 999:
    total += num
    cont += 1
    num = int(input('Digite outro número [999 para encerrar]: '))
print('Você digitou {} numeros e a soma deles é {}'.format(cont, total))