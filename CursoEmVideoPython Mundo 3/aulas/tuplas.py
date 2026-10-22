# Tuplas são imutáveis!
lanche = ('Hambúrger', 'Suco', 'Pizza','Pudim')
'''print(lanche[1])'''

'''for comida in lanche:
    print(f'Eu comi {comida}')'''

for cont in range(0,len(lanche)):
    print(f'Eu comi {lanche[cont]} na posiçao {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}')