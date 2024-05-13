#mostrar na tela o antecessor e sucessor do numero digitado

n = int(input('Digite um número inteiro (número sem virgula/ponto): '))

suc = n + 1
ant = n - 1

print('O número digitado é {}. O número antecessor à ele é {} e o sucessor é {}'.format(n, ant, suc))

