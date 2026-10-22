lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'A lista completa ficou: {lista}')
print(f'A lista de números PARES fiocu: {pares}')
print(f'A lista de números IMPARES ficou: {impares}')