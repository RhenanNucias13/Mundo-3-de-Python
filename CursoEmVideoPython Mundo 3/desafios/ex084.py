dados = []
galera = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'Você cadastrou {len(galera)} pessoas.')
print(f'O MAIOR peso foi de {maior}Kgs. Peso de: ',end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O MENOR peso foi de {menor}Kgs. Peso de: ',end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
