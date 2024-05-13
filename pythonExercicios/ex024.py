#ler o nome de uma cidade e ver se começa com nome SANTO

cid = str(input('Digite o nome da sua cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')

