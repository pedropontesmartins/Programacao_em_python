import getpass 
def recebe_str(mensagem):
    while True:
        try:
            texto = str(input(mensagem))
            break        
        except:
            print("Valor invalido!")
    return texto
def recebe_senha(mensagem):
    while True:
        try:
            senha = getpass.getpass(mensagem)
            break
        except:
            print("Valor invalido!")
    return senha
def recebe_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            break
        except:
            print("Valor invalido!")
    return numero

