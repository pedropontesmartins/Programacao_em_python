import pyfiglet
 
def msg_inicial():
    print("Seja bem vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format ("COTA-FRETE", font= "speed")
    m2= pyfiglet.figlet_format ("Sua melhor rota!", font= "cybermedium")
    print("\033[36m" + mensagem + "\033[0m")
    print(m2)
def msg_login_ini():
    print("\033[34m###############################\033[0m")
    print("<<<<<< LOGAR NO SISTEMA >>>>>>>")
    print("\033[34m###############################\033[0m")
def msg_menu_pricipal():
    print("\033[34m#################################################\033[0m")
    print("<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>")
    print("\033[34m#################################################\033[0m")
    print("<| SAIR - 0| CALCULADORA - 1| CALCULA FRETE - 2|>\n")
    
    