#VARIOS NUMEROS COM FLAGS

num = cont = soma = 0

while num != 999:
    num = int(input('Digite um número (999 para encerrar):  '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Você digitou {cont} e a soma deles é {soma}')


