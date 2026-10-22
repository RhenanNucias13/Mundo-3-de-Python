'''num = [2,5,9,1]
num[2] = 3 # altera um valor da lista
num.append(7) # adiciona um valor na lista
num.sort(reverse=True) # ordena a lista de forma reversa
num.insert(2,0) # adiciona um valor em um indice especifico
# num.pop() # remove o valor final (ou um especifico)
if 4 in num: # remove o valor SE ele estiver presente na lista
    num.remove(4)
else:
    print('Nao achei o número 4')
print(num)
print(f'essa lista tem {len(num)} elementos')'''

valores = []
'''valores.append(4)
valores.append(2)
valores.append(8)'''

for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))

for c,v in enumerate(valores):
    print(f'Na posição {c} achei o valor {v}')
