

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Primeiro nome {}'.format(nome[0]))
print('Ultimo nome {}'.format(nome[len(nome)-1]))
