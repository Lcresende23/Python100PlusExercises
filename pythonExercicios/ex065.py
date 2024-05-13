media = cont = soma = 0
r = 'Ss'
maior = 0
menor = 0
while r in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Deseja continuar [S/N]')).upper().strip()[0]
media = soma / 2
print('FIM! Foram digitados {} números e a média deles é {}. O Maior número é o {} e o menor é o {}'
      ''.format(cont, media, maior, menor))
