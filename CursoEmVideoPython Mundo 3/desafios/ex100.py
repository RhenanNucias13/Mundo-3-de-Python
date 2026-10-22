from random import randint
from time import sleep

lista = []
def random(lista):
    print('Sorteando os 5 valores da lista: ',end='')
    for c in range(1,6):
        nums = randint(1,10)
        lista.append(nums)
        print(nums,end=' ')
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores da {lista} ,temos {soma}')


random(lista)
somapar(lista)