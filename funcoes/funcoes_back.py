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
    list = ["Criar senha somente númerica", "Criar senha somente letras", "Criar senha somente alfanúmerica", "Sair"]
    i = 1
    for op in list:
        print(f"{i}-{op}\n")
        i += 1
    resposta =(int(input("Digite sua resposta(1, 2, 3): ")))
    if resposta == 1:
        gerar_somentenumeros()
    elif resposta == 2:
        gerar_somenteletras()
    elif resposta == 3:
        gerar_caracteres()
    else:
        linha()
        print("Opção invalida, tente 1, 2 ou 3")
    
def gerar_somentenumeros():
    linha()
    print("Gostaria de uma senha com: ")
    print("4 Digitos - 6 Digitos - 8 Digitos: ")
    num = int(input())
    while True:
        if num == 4:
            print(random.sample(range(0, 10), num))
        elif num == 6:
            print(random.sample(range(0, 9),num))
        elif num == 8:
            print(random.sample(range(0, 9), num))
        else:
            print("Erro ! Digite somente uma das 3 opções.")
        break
        

def gerar_somenteletras(quantidade = 8):
    linha()
    quantidade = int(input("Digite a quantidade de caracteres para sua senha[MIN 4 / MAX 18]: "))
    linha()
    #string.ascii pega todas as letras a-z grande e pequena
    #string.digits pega todos os num de 0-9
    while True:
        if  4 <= quantidade <= 18:
            caracteres = string.ascii_letters + string.digits
            senha = ''.join(random.choice(caracteres) for _ in range(quantidade))
            print(senha)
        else:
            print("Valor abaixo de do min ou maior que o maximo permitido, tente novamente.")
        break

def gerar_caracteres():
    print("s")
    
def menu():
    titulo()
    n = opcoesmenu()
    


        
    