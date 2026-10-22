times = ('Palmeiras','Flamengo','Fluminense','Atlhetico-PR',
         'RB-Bragantino','Coritiba','São Paulo','Bahia','Cruzeiro'
         ,'Botafogo','Vitória','Atletico-MG','Internacional','Grêmio',
         'Corinthians','Vasco','Santos','Mirassol','Remo','Chapecoense')
print(f'Tabela do Brasileirão série A: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'OS 4 últimos são: {times[-4:]}')
print(f'Tabela em ordem alfabética: {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense")+ 1} posição.')