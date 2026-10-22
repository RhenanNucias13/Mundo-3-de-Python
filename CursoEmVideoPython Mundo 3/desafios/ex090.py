aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
print('-=' * 30)
print(f'- Nome do aluno(a): {aluno["nome"]}')
print(f'- Média do aluno(a): {aluno["media"]}')
if aluno['media'] >= 6:
    aluno['estado'] = 'APROVADO!'
elif 5 <= aluno['media'] < 6:
    aluno['estado'] = 'RECUPERAÇÃO'
else:
    aluno['estado'] = 'REPROVADO!'
print(f'Situação do aluno(a): {aluno["estado"]}')