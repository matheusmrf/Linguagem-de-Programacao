from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas Cadastradas', 'Sair do Sistema'])
    if resposta == 1:
        #Opcao de cadastrar
        cabecalho('Novo Cadastro')
        nome = str(input('Digite seu nome: '))
        idade = leiaInt('Digite sua idade: ')
        sexo = input('Digite seu sexo (m/f): ')
        email = input("Digite seu email: ")
        cadastrar(arq, nome, idade, sexo, email)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        cabecalho('Voltando para o menu principal... ')
        break
    else:
        print('\033[31mErro! Digite uma opcao válida.\033[m')
    sleep(2)