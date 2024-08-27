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
    num = int(input('Digite a quantidade de números que você quer na sua senha: '))
    print(random.sample(range(0, 10), num))
    sleep(1)
    
def gerar_alfanumerica():
    print("x")

def gerar_alfabetica():
    print("s")
    
def menu():
    titulo()
    opcoesmenu()
    resp = int(input("Digite sua resposta: "))
    if resp == 1:
        gerar_numeros()
    elif resp == 2:
        gerar_alfanumerica()
    elif resp == 3:
        gerar_alfabetica()

    
        
    