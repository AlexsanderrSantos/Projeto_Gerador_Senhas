# printa linha de acordo com o texto
def linha(tam = 42):
    print('-' * tam)
    
def titulo():
    linha()
    print(f"Gerador de Senhas v.1".center(42))
    linha()

def cabecalho(lst):
    titulo()
    pos = 1
    for i in lst:
        print(f" {pos} - {i}\n")
        pos += 1
    resp = input("Digite sua opção: ")