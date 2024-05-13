def aumentar(n =0 , taxa = 0,  formato=False):
    n += n * (10/100)
    return n if formato is False else moeda(n)


def diminuir(n = 0, taxa = 0, formato=False):
    n -= n * (13/100)
    return n if formato is False else moeda(n)

def dobro(n = 0, formato=False):
    n *= 2
    return n if not formato else moeda(n)

def metade(n = 0, formato=False):
    n = n/2
    return n if not formato else moeda(n)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
