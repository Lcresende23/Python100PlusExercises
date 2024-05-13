from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)

while True:
    resposta = menu(['VISUALIZAR LISTA', 'CADASTRAR', 'SAIR DO SISTEMA'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do programa... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m ')
        sleep(2)


