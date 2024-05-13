# Ficha do Jogador

def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')


nome = str(input('Nome: '))
gol = str(input('Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)

