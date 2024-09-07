import string
import random
import pdb
from time import sleep


# printa Linha de acordo com o texto
def Linha(tam = 42):
    print('-' * tam)
    
def Titulo():
    Linha()
    print(f"Easy Password v.1".center(42))
    Linha()


def Opcoesmenu():
    list = ["Criar senha somente númerica", "Criar senha somente letras", "Criar senha somente alfanúmerica", "Sair"]
    i = 1
    for op in list:
        print(f"{i}-{op}\n")
        i += 1
    resposta = input("Digite sua resposta(1, 2, 3, 4): ")
    resposta = Valida_numeros(resposta)
    if resposta == 1:
        Gerar_somentenumeros()
    elif resposta == 2:
        Gerar_somenteletras()
    elif resposta == 3:
        Gerar_alfanumerico()
    elif resposta == 4:
        return True
    else:
        print("Digite uma opção valida !")
            
    
def Gerar_somentenumeros():
    opc =[4, 6, 8]
    Linha()
    print("Gostaria de uma senha com: ")
    print("[4 Digitos - 6 Digitos - 8 Digitos]")
    resposta = input("Sua resposta: ")
    num = Valida_numeros(resposta)
    Linha()
    while True:
        if num in opc:
            senha = (random.sample(range(0, 10), num))
            for indice, numero in enumerate(senha):
                print(f"{numero}", end="\n" if indice == len(senha) -1 else "")
        else:
            print("Erro ! Digite somente uma das 3 opções.")
        sleep(1)
        break
        

def Gerar_somenteletras(quantidade = 8):
    Linha()
    quantidade = input("Digite a quantidade de caracteres para sua senha[MIN 4 / MAX 18]: ")
    quantidade = Valida_numeros(quantidade)
    #string.ascii pega todas as letras a-z grande e pequena
    #string.digits pega todos os num de 0-9
    while True:
        if  4 <= quantidade <= 18:
            caracteres = string.ascii_letters
            senha = ''.join(random.choice(caracteres) for _ in range(quantidade))
            Linha()
            print(senha)
        else:
            Linha()
            print("Digite uma quantidade válida!")
        sleep(1)
        break

def Gerar_alfanumerico():
    Linha()
    quantidade = input("Digite a quantidade de caracteres para a senha:[MIN 4 / MAX 18] ")
    quantidade = Valida_numeros(quantidade)
    while True:
        if 4 <= quantidade <= 18:
            caracteres = string.ascii_letters + string.digits
            senha = "".join(random.choice(caracteres) for _ in range(quantidade))
            Linha()
            print(senha)
        else:
            print("Digite uma quantidade válida!")
        sleep(1)
        break


def Valida_numeros(opc):
        try:
            numero_inteiro = int(opc)
        except(TypeError,ValueError):
            Linha()
            print("Ocorreu um erro de tipo ou valor")
            return False
        except(KeyboardInterrupt):
            Linha()
            print("O usuário não quis digitar")
        else:
            return numero_inteiro


def Menu():
    while True:
        Titulo()
        escolha = Opcoesmenu()
        if escolha == True:
            break

Menu()        


        
    