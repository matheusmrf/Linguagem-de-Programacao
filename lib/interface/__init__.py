# Função que verifica se a entrada de dados no menu é do tipo Int
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\003[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\003[31mUsuário preferiu nao digitar esse número.\033[m')
            return 0
        else:
            return n

# Função que ajuda na formatação do menu
def linha():
    return '-' * 42

# Função que gera o cabeçalho do menu
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# Função que gera o menu (recebe como parâmetro uma lista de itens do menu)
def menu(lista):
    cabecalho('Menu')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opcao: \033[m')
    return opc