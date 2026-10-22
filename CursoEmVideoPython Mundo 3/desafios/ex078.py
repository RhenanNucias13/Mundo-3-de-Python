lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'você digitou os valores: {lista}')
print(f'O MAIOR valor digitado foi {max(lista)} nas posições', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f' {i}...', end='')
print()
print(f'O Menor valor digitado foi {min(lista)} nas posições', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f' {i}...',end='')
print()