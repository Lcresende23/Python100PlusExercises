# cadastro de jogador de futebol

jogador = dict()
partidas = list()
jogador.clear()
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantidade de partidas do {jogador["nome"]}: '))
print('_' * 30)

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('_' * 30)
print(jogador)
print('_' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('_' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols.')
print(f'Fez um total de {jogador["total"]} gols nas {len(jogador["gols"])} partidas')




