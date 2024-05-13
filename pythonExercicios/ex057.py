n = 1
sexo = str(input('Digite o seu sexo {M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos: Tente novamente. Digie seu sexo [M/F]: ')).strip().upper()[0]

print('\033[33mO sexo {} foi registrado com sucesso'.format(sexo))
