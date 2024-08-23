def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    

def menu(lst):
    cabecalho('Menu Principal')
    c = 1
    for item in lst:
        print(f"\033[33:m{c}\033[m - \033[34m{item}\033[m" )
        c += 1
    print(linha())
    opc = leiaint("\033[32mSua Opção: \033[m")
    return opc


def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except(TypeError,ValueError):
            print(f'\033[31mErro! entrada de dados do tipo incorreto.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mO usúario preferiu não digitar valores.\033[m')
            return 0
        else:
            return n
    
    