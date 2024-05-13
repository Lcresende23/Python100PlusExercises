# Função que descobre o maior
from time import sleep


def maior(*valores):
        print('=' * 84)
        print(f'{v} Foram informados. Ao todo {len(valores)} valores informados.', flush=False)
        print(f'O maior valor foi {max(valores)}.', flush=False)
        sleep(1)
        



maior(3, 5, 6, 18, 2, 1)
maior(3, 12, 34, 2, 1, 5, 12, 56, 33)
maior(1)

