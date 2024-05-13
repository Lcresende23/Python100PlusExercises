def aumentar(n=0, taxa=0):
    n += n * (10/100)
    return n


def diminuir(n=0, taxa=0):
    n -= n * (13/100)
    return n


def dobro(n=0):
    n *= 2
    return n


def metade(n=0):
    n = n/2
    return n


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
