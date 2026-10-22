from ex109 import moeda

p = float(input('Digite seu preço:R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formatar= True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formatar= True)}')
print(f'Aumentando 10%, temos {moeda.aumento(p,10, formatar= True)}')