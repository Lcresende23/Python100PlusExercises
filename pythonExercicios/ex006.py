#mostrar o dobro, triplo e raiz quadrada de um numero

n = int(input('Digite um numero inteiro: '))

d = n * 2
t = n * 3
raiz = n ** (1/2)

print('O número digitado foi {} \nO dobro dele é {} \nO triplo é {} \nA raiz quadrada dele é {:.2f}'.format(n, d, t, raiz))
