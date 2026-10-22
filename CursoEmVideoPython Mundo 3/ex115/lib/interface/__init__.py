def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Por Favor digite um valor inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print(print('\n\033[0;31mERRO! O Usuário preferiu não digitar.\033[m'))
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = LeiaInt('Digite sua opção:')
    return opc