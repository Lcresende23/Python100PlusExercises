# Funções com modularização formatado
from utilidadecev import moeda
from utilidadecev import dado

num = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(num, 50, 15)
