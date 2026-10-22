'''brasil = []
estado1 = {'uf': 'Distrito Federal', 'sigla': 'DF'}
estado2 = {'uf': 'Goiás', 'sigla': 'GO'}
brasil +=[estado1,estado2]   #dicionarios em listas
print(brasil[1]['uf'])'''

brasil = list()
estado = dict()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O estado {k} tem a sigla {v}')