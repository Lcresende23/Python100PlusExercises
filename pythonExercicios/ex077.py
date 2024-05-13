lista = ('Casa', 'Carro', 'Jogo', 'Pedra', 'Parede', 'Jogador', 'Praticar', 'Carreta',
         'Missel', 'Basquete', 'Marea')

for c in lista:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
