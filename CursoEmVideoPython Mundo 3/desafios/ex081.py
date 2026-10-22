lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse= True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O número 5 está presente na lista!')
else:
    print('O número 5 não está presente na lista!')