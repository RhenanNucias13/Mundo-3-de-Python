from ex107.moeda import desconto


def metade(preço=0, formatar = False):
    res = preço / 2
    return res if not formatar else moeda(res)


def dobro(preço=0, formatar = False):
    res = preço * 2
    return res if not formatar else moeda(res)


def aumento(preço=0,taxa=0, formatar = False):
    res = preço + (preço * taxa / 100)
    return res if not formatar else moeda(res)

def desconto(preço=0,taxa=0, formatar = False):
    res = preço - (preço * taxa / 100)
    return res if not formatar else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0,taxaa=10,taxar=5):
    print('-' * 30)
    print('RESUMO DO PREÇO'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{moeda(preço)}')
    print(f'Metade do valor: \t{moeda(metade(preço))}')
    print(f'Dobro do valor: \t{moeda(dobro(preço))}')
    print(f'{taxaa}% de TAXA: \t\t{aumento(preço,taxaa, True)}')
    print(f'{taxar}% de DESCONTO: \t{desconto(preço,taxar, True)}')
    print('-' * 30)