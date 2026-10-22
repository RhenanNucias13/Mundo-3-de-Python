from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{'MEGA SENA':^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer comprar?: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 5 ,f'SORTEANDO {quant} JOGOS.', '-=' * 5)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('BOA SORTE!')