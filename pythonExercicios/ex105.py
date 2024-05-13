
def notas(*valores, sit=False):
    """
    -> Funçao para analisar notas e situações de vários alunos
    :param valores: Uma ou mais notas e situações de varios alunos
    :param sit: valor opcional, apresentar ou não a situação do aluno
    :return: retorna as informações para a variavel resp
    """
    ficha = dict()
    ficha['total'] = len(valores)
    ficha['maior'] = max(valores)
    ficha['menor'] = min(valores)
    ficha['média'] = sum(valores)/len(valores)
    if ficha['média'] >= 7:
        ficha['situação'] = 'Boa'
    elif ficha['média'] >= 5:
        ficha['situação'] = 'Regular'
    else:
        ficha['situação'] = 'Ruim'


    return ficha

resp =  notas (5.5, 10, 10, 7.6, sit=True)
print(resp)
