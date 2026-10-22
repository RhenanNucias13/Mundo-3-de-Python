def notas(*n,sit=False):
    '''
    -> Função para calcular a média de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: situação do aluno (opcional)
    :return: retorna em forma de dicionário a situação da turma
    '''
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maiornota'] = max(n)
    aluno['menornota'] = min(n)
    aluno['media'] = sum(n) / len(n)
    if sit:
        if aluno['media'] >= 7:
            aluno['situaçao'] = 'BOA!'
        elif aluno['media'] >= 5:
            aluno['situaçao'] = 'MAIS OU MENOS.'
        else:
            aluno['situaçao'] = 'RUIM!'
    return aluno


resp = notas(9,4,9,6,7, sit=True)
print(resp)
#help(notas)