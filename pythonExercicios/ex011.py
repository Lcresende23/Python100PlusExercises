# descobrir a area para pintar a parede

alt = float(input('Informe a altura da parede: '))
larg = float(input('Informe a largura da parede: '))

area = larg * alt

print('A sua parede tem uma dimensão de {} x {} e a área dela é de {}m²'.format(alt, larg, area))
print('A quantidade necessária de tinta para pintar a parede é de {} litros de tinta.'.format(area/2))
