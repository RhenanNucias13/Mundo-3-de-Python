from datetime import datetime
cidadao = dict()
cidadao['nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento: '))
cidadao['idade'] = datetime.now().year - nasc
cidadao['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cidadao['ctps'] != 0:
    cidadao['contratação'] = int(input('Ano da contratação: '))
    cidadao['salario'] = float(input('Salário: '))
    cidadao['aposentadoria'] = cidadao['idade'] + ((cidadao['contratação'] + 35) - datetime.now().year)
print('-=' * 20)
for k,v in cidadao.items():
    print(f'-  O {k} tem o valor de {v}')