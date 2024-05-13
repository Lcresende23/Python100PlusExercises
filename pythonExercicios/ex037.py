#Conversão de bases
num = int(input('Digite um número inteiro: '))

print('Escolha qual será a conversão:\n'
      '1 - Binário\n2 - Octal\n3 - Hexadecimal')
opçao = int(input('Qual opção você deseja: '))

if opçao == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))

elif opçao ==2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))

elif opçao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))

else:
    print('Opção Inválida!')



