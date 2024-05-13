# Verificando site
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')

except urllib.error.URLError:
    print('Erro na conexão com o site do Youtube')

else:
    print('Consegui conectar no site do Youtube')

