import string
import random
from time import sleep

# printa linha de acordo com o texto
def linha(tam = 42):
    print('-' * tam)
    
def titulo():
    linha()
    print(f"Easy Password v.1".center(42))
    linha()


def opcoesmenu():
    list = ["Criar senha somente númerica", "Criar senha somente letras", "Criar senha somente alfanúmerica", "Sair"]
    i = 1
    for op in list:
        print(f"{i}-{op}\n")
        i += 1
    resposta =(int(input("Digite sua resposta(1, 2, 3, 4): ")))
    if resposta == 1:
        gerar_somentenumeros()
    elif resposta == 2:
        gerar_somenteletras()
    elif resposta == 3:
        gerar_alfanumerico()
    elif resposta == 4:
        return True
    else:
        linha()
        print("Opção invalida, tente 1, 2 ou 3")
            
    
def gerar_somentenumeros():
    linha()
    print("Gostaria de uma senha com: ")
    print("4 Digitos - 6 Digitos - 8 Digitos: ")
    num = int(input())
    linha()
    while True:
        if num == 4:
            print(random.sample(range(0, 10), num))
        elif num == 6:
            print(random.sample(range(0, 9),num))
        elif num == 8:
            print(random.sample(range(0, 9), num))
        else:
            print("Erro ! Digite somente uma das 3 opções.")
        sleep(1)
        break
        

def gerar_somenteletras(quantidade = 8):
    linha()
    quantidade = int(input("Digite a quantidade de caracteres para sua senha[MIN 4 / MAX 18]: "))
    #string.ascii pega todas as letras a-z grande e pequena
    #string.digits pega todos os num de 0-9
    while True:
        if  4 <= quantidade <= 18:
            caracteres = string.ascii_letters
            senha = ''.join(random.choice(caracteres) for _ in range(quantidade))
            linha()
            print(senha)
        else:
            print("Valor abaixo de do min ou maior que o maximo permitido, tente novamente.")
        sleep(1)
        break
#caracteres = string.ascii_letters + string.digits
#senha = ''.join(random.choice(caracteres) for _ in range(quantidade))
def gerar_alfanumerico():
    linha()
    quantidade = int(input("Digite a quantidade de caracteres para a senha:[MIN 4 / MAX 18] "))
    while True:
        if 4 <= quantidade <= 18:
            caracteres = string.ascii_letters + string.digits
            senha = "".join(random.choice(caracteres) for _ in range(quantidade))
            linha()
            print(senha)
        else:
            print("Valor abaixo do min ou maior que o maximo permitido, tente novamente.")
        sleep(1)
        break
def menu():
    while True:
        titulo()
        escolha = opcoesmenu()
        if escolha == True:
            break

        


        
    