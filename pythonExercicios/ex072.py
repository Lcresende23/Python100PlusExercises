numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')


while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha >= 0 and escolha <=20:
         print(f'Você digitou o número {numeros[escolha]}')
    else:
        print('Tente novamente. ', end='')

    r = ' '
    while r not in 'SN':
        r = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break

print('\nFINALIZADO')













