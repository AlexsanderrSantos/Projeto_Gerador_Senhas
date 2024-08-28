import string
import random
from time import sleep

# printa linha de acordo com o texto
def linha(tam = 42):
    print('-' * tam)
    
def titulo():
    linha()
    print(f"Gerador de Senhas v.1".center(42))
    linha()


def opcoesmenu():
    list = ["Criar senha númerica", "Criar senha alfanúmerica", "Criar senha alfabética", "Sair"]
    i = 1
    for op in list:
        print(f"{i}-{op}\n")
        i += 1
    
def gerar_numeros():
    opcoes = [4,6,8]
    print("Gostaria de uma senha com:\n")
    print("4 Digitos - 6 Digitos - 8 Digitos: ")
    num = int(input())
    if num not in opcoes:
        print("Digite uma das 3 opções validas !")
    else:
        if num == 1:
            return(random.sample(range(0, 10), num))
        elif num == 2:
            return(random.sample(range(0, 9),num))
        elif num == 3:
            return(random.sample(range(0, 9), num))
        else:
            print("Erro ! Digite somente uma das 3 opções.")
        

def gerar_alfanumerica(tam=10):
    #string.ascii pega todas as letras a-z grande e pequena
    #string.digits pega todos os num de 0-9
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(10))
    return senha

def gerar_alfabetica():
    print("s")
    
def menu():
    titulo()
    opcoesmenu()
    resp = int(input("Digite sua resposta: \n"))
    if resp == 1:
        print(gerar_numeros())
    elif resp == 2:
        print(gerar_alfanumerica(6))
    elif resp == 3:
        gerar_alfabetica()


        
    