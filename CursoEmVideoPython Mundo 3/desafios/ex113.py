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

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Por Favor digite um valor inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print(print('\n\033[0;31mERRO! O Usuário preferiu não digitar.\033[m'))
            return 0
        else:
            return n

inteiro = LeiaInt('Digite um número Inteiro: ')
real = LeiaFloat('Digite um número Real: ')
print(f'Os valores digitados foram {inteiro} e {real}')