cont = ('zero','um','dois','tres','quatro','cinco','seis',
        'sete','oito','nove','dez','onze','doze','treze',
        'catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente Novamente...', end='')
print(f'O número que você digitou foi o {cont[n]}')