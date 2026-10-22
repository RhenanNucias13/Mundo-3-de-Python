lista = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome,[n1,n2],media])
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'{"N°":<4}{"ALUNO":<10}{"MÈDIA":>8}')
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Quer ver a nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(lista )-1:
        print(f'A nota do aluno(a) {lista[opc][0]} foi de {lista[opc][1]}')