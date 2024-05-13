#Calculo de desconto

print('====LOJINHA DO LUQUINHAS====')

gasto = float(input('Quanto você gastou na minha loja? '))

print('Formas de pagamento:\n1 - À vista dinhero/cheque\n2 - À vista no cartão\n3 - 2x no cartão\n'
      '4 - 3x ou mais no cartão ')
opçao = int(input('Qual será a forma de pagamento? '))


if opçao == 1:
    total = gasto - (gasto * 10/100)
    print('O valor de sua compra de R${} com 10% de desconto ficou em R${:.2f}'.format(gasto, total))

elif opçao ==2:
    total = gasto - (gasto * 5/100)
    print('O valor de sua compra de R${} com 5% de desconto ficou em R${:.2f}'.format(gasto, total))

elif opçao == 3:
    total = gasto
    parcela = total / 2
    print('O valor de sua compra de R${} será parcelado em 2x de R${} SEM JUROS'.format(gasto,parcela))
elif opçao == 4:
    total = gasto + (gasto * 20/100)
    totalparc = int(input('Quantas parcelas deseja?'))
    parcela = total / totalparc
    print('O valor de sua compra de R${} será parcelada em {}x com valor de R${} COM JUROS'.format(gasto,totalparc, parcela))

else:
    total = 0
    print('Erro! Opção inválida de pagamento.')
    print('Sua compra de R${} será de R${} no final.'.format(gasto, gasto))