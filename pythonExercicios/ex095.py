# cadastro de jogador de futebol aprimorado

jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantidade de partidas do {jogador["nome"]}: '))
    partidas.clear()
    print('_' * 30)
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if r not in 'SN':
            print('ERRO! Digite apenas S ou N')
    if r == 'N':
        break
print('_' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar busca): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {1} fez {g} gols')
    print('_' * 30)
print('Volte Sempre!')



