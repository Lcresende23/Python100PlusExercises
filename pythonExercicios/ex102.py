# Função para fatorial

def fatorial(num, show=False):
    """
    >> Calculo do Fatorial
    :param num: número a ser fatorado
    :param show: SE SHOW tiver em TRUE ele mostra o calculo. SE tiver em FALSE, mostra apenas o resultado.
    :return: Retorna o resultado  de num para PRINT
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


num = int(input('Qual número quer fatorar? Digite: '))
print(fatorial(num, show=True))