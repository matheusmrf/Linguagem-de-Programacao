# Nome: Bruno Pena Baeta e Matheus Rangel de Figueiredo
# Professor: Hugo Bastos de Paula
# Matéria: Linguagens de Programação

from lib.interface import *
from lib.arquivo import *
from time import sleep


########################################### Funcao 1 ######################################################

def func1():
    # Formulário do produto
    global preco, qtde, menor
    nome = input('Digite o nome do produto (string): ')
    t = True
    while t:
        try:
            qtde = input('Digite a quantiadade desse produto no estoque (int): ')
            int(qtde)
            t = False
        except:
            print(f"'{qtde}' não é do tipo int")

    t = True
    while t:
        try:
            preco = input('Digite o preço desse produto (float): ')
            float(preco)
            t = False
        except:
            print(f"'{preco}' não é do tipo float")

    t = True
    while t:
        try:
            menor = input('Esse produto pode ser consumido por menores de idade? (boolean): ')
            bool(menor)
            t = False
        except:
            print(f"'{menor}' não é do tipo boolean")

    # Criando dicionário do produto
    produto = {
        "nome": nome,
        "qtde": qtde,
        "preco": preco,
        "menor": menor
    }

    # Apresentando valores criados
    print(f"""Produto criado:
    Nome: {produto["nome"]}
    Quantidade no estoque: {produto["qtde"]}
    Preço: {produto["preco"]}
    Pode ser consumido por menores de idade? {produto["menor"]}
  """)


########################################### Funçao 2 ######################################################


# Declarando o vetor de Fibonacci
sequencia = []


# Função recursiva que é chamada pela Função 2 e imprime a sequência de Fibonacci
def fibonacci(contador, n1, n2):
    if contador < 1:
        return 0
    else:
        sequencia.append(n1 + n2)
    return fibonacci(contador - 1, n2, n1 + n2)


# FUNÇÃO 2: Função que apresenta a sequencia de Fibonacci usando recursividade e vetores
def func2():
    q = int(input('Digite a quantidade de termos que deverão aparecer na sequência: '))
    if q < 1:
        print("Digite um número válido.")
    elif q < 2:
        sequencia.append(1)
    elif q < 3:
        sequencia.append(1)
        sequencia.append(1)
    else:
        sequencia.append(1)
        sequencia.append(1)
        fibonacci(q - 2, 1, 1)
    print(sequencia)

########################################### Funçao 3 ######################################################

def func3():
    arq = 'cadastros.txt'

    if not arquivoExiste(arq):
        criarArquivo(arq)

    while True:
        resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas Cadastradas', 'Voltar para o menu principal'])
        if resposta == 1:
            # Opcao de cadastrar
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



########################################### MENU PRINCIPAL ######################################################

while True:
    resposta = menu(['Funcao de criar produto (tipos de dados e dicionários', 'Função recursiva que apresenta a '
                                                                              'sequencia de Fibonacci (recursividade '
                                                                              'e vetores)', 'Função para cadastrar '
                                                                                            'clientes em um arquivo '
                                                                                            'externo (manipulação de '
                                                                                            'arquivos)',
                     'Sair do Sistema'])
    if resposta == 1:
        func1()
    elif resposta == 2:
        func2()
    elif resposta == 3:
        func3()
    elif resposta == 4:
        cabecalho('Encerrando o programa. ')
        break
    else:
        print('\033[31mErro! Digite uma opcao válida.\033[m')
    sleep(2)
