#dissecar uma variavel

n = input('Digite algo: ')
print('Qual o tipo primitivo desse valor?', type(n))
print('O valor digitado é Alfanumérico?', n.isalnum())
print('O valor digitado é Alfa?', n.isalpha())
print('O valor digitado é todo em minúsculo?', n.islower())
print('O valor digitado é todo em maiúsculo?', n.isupper())
