def aumentar(n =0 , taxa = 0,  formato=False):
    """
    -> Calcula o aumento de um preço
    :param n: valor a ser ajustado
    :param taxa: percentual de almento
    :param formato: formatação correta de números
    :return: retorna o valor a ser mostrado
    """
    n = n + (n * taxa/100)
    return n if formato is False else moeda(n)


def diminuir(n = 0, taxa = 0, formato=False):
    n = n - (n * taxa/100)
    return n if formato is False else moeda(n)

def dobro(n = 0, formato=False):
    n *= 2
    return n if not formato else moeda(n)

def metade(n = 0, formato=False):
    n = n/2
    return n if not formato else moeda(n)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxaa=20, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'A metade do preço: \t{metade(n, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(n, taxaa, True)}')
    print(f'Com {taxar}% de redução: {diminuir(n, taxar, True)}')
    print('_' * 30)

