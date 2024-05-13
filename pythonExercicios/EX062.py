print('\033[31mGERADOR DE PA\033[m')
print('-=-'*8)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <=total:
        print('{}→ '.format(termo), end='')
        termo += razao
        cont += 1

    print('Pausa')
    mais = int(input('Deseja continuar? Digite 0 para encerrar.'))
print('FIM! Foram mostradas {} progressões'.format(total))

