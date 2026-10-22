from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criaarquivo(arq)


while True:
    resposta = menu(['Ver Pesoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('ENCERRANDO....')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)