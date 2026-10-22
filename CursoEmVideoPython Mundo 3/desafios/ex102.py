def fatorial(num, show = False):
    '''
    -> Calcula o fatorial de um número.
    :param num: número a ser caculado.
    :param show: (opcional) Mostrar ou não os processos
    :return: Retorna o valor do fatorial de n.
    '''
    f = 1
    for c in range(num,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f
print(fatorial(5,True))
# help(fatorial)