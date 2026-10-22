'''teste = list()
teste.append('Rhenan')
teste.append(16)
galera = list()
galera.append(teste[:])         <-- lista composta
teste[0] = 'Duda'
teste[1] = 17
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Maria', 89], ['Gustao', 22],['Pedro', 33]]
# print(galera[3][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} pessoas MAIORES e {totmenor} pessoas MENORES de idade.')