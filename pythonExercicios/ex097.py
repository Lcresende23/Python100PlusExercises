# um print especial

def escreva(txt):
    tam = len(txt) + 4
    print('_' * tam)
    print(f'  {txt}')
    print('_' * tam)


escreva('Lucas é lindo')
escreva('Lucas manja de Python')
escreva('Hello World')
