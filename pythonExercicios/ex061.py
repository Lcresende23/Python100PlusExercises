print('\033[31mGERADOR DE PA\033[m')
print('-=-'*8)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1

while cont <=10:
    print('{}→ '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM!')
