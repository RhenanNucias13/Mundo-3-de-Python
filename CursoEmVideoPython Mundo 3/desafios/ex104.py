def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('\033[0;31mERRO! Digite um valor de número inteiro.\033[m')
        if ok:
            break
    return valor
        
n = leiaint('Digite um número: ')
print(f'Você digitou o valor {n}.')