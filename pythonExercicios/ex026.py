#ler uma frase e mostrar se tem letra A

frase = str(input('Digite uma frase: ')).upper().strip

print('Quantas letras A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))




