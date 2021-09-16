from lib.interface import *

# Função que verifica a existência do arquivo
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Função que cria o arquivo (recebe o nome do arquivo como parâmetro)
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criacao do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

# Função que lê o arquivo (recebe como parâmetro o nome do arquivo)
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:<25}{dado[2]:<20}{dado[3]:<15}')
    finally:
        a.close()

# FUnção que escreve os dados no arquivo (recebe como parâmetro o nome do arquivos e os dados a serem escritos)
def cadastrar(arq, nome, idade, sexo, email):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade};{sexo};{email}\n')
        except:
            print('Houve um erro na hora de inserir os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()


