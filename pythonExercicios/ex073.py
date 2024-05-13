#tupla com timer brasileirao

times = ('Palmeiras', 'Grêmio', 'Atletico Mineiro', 'Flamengo',
         'Botafogo', 'Bragantino', 'Fluminense', 'Atletico PR',
         'Internacional', 'Chapecoense')
print('_'*150)
print(f'Os cinco primeiros colocados do brasileirão:  {times[:5]}')
print('_'*150)
print(f'Os ultimos 4 colocados da tabela: {times[-4:]}')
print('_'*150)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('_'*150)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
print('_'*150)

