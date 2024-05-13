
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = 0
tot = 0

while opcao != 5:
    print('Qual operação deseja realizar?\n'
          '[ 1 ] SOMA\n'
          '[ 2 ] MULTIPLICAR\n'
          '[ 3 ] MAIOR\n'
          '[ 4 ] NOVOS NÚMEROS\n'
          '[ 5 ] SAIR DO PROGRAMA\n')
    opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))
    if opcao == 1:
        tot = n1 + n2
        print('A opção escolhida foi {} e a soma de {} + {} = {}'.format(opcao, n1, n2, tot))

    elif opcao == 2:
        tot = n1 * n2
        print('A opção escolhida foi {} e a multiplicação de {} * {} = {}'.format(opcao, n1, n2, tot))

    elif opcao == 3:
        if n1 > n2:
            tot = n1
            print('Você digitou {} e {} e o maior entre eles é {}'.format(n1, n2, tot))
        else:
            tot = n2
            print('Você digitou {} e {} e o maior entre eles é {}'.format(n1, n2, tot))
    elif opcao == 4:
        print('Escolha os números')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('\033[31mFinalizando...\033[m')

print('\033[34mPrograma encerrado! Obrigado por utilizar.')