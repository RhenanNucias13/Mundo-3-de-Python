def soma(*numeros):
    s = 0
    for v in numeros:
        s += v
    print(f'A soma entre {numeros} é de {s}')

soma(4, 5, 2, 1)

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [2, 5, 7, 3, 9, 8]
dobra(valores)
print(valores)