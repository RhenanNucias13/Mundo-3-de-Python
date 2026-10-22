from time import sleep
def maior(*n):
    cont = mai = 0
    print('-=' * 20)
    print('Analisando valores passados...')
    for valor in n:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'E o maior entre eles foi {mai}.')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()