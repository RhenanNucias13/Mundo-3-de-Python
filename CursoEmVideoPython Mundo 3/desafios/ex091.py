from random import randint
from time import sleep
from operator import itemgetter
resultados = {'jogador1': randint(1,6),
              'jogador2': randint(1,6),
              'jogador3': randint(1,6),
              'jogador4': randint(1,6)}
podio = []
for k,v in resultados.items():
    print(f'O {k} tirou {v} no dado.')
podio = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print(f'{"RANKING": ^30}')
for i,v in enumerate(podio):
    print(f'{i+1}° lugar {v[0]} com: {v[1]} pontos.')