import random

# printa linha de acordo com o texto
def linha(tam = 42):
    print('-' * tam)
    
def titulo():
    linha()
    print(f"Gerador de Senhas v.1".center(42))
    linha()


def opcoesmenu():
    list = ["Gerar senha 4 digitos", "Gerar senha 6 digitos", "Gerar senha 8 digitos"]
    i = 1
    for op in list:
        print(f"{i}-{op}\n")
        i += 1
    
    
def cabecalho():
    titulo()
    opcoesmenu()
    resp = int(input("Digite sua resposta: "))
    gerarnumeros(resp)
    
def gerarnumeros(opc):
    print(opc)
    if opc == 1:
        print(random.sample(range(0, 10), 4))
    elif opc == 2:
        print(random.sample(range(0,10), 6))
    elif opc == 3:
        print(random.sample(range(0,10), 8))
    elif opc == 4:
        return "break"
        
    