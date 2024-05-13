#validando expressões matematicas

expr = str(input('Digite sua expressão: '))
lista = []

for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida')