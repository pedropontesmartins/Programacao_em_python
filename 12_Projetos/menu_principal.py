import mod_msg
import mod_inputs
import calculadora
import login
def recebe_opção():
    while True:
        mod_msg.msg_menu_pricipal()
        opcao =mod_inputs.recebe_int("Insira sua opção - ")
        match opcao:
            case 0:
                print("Adeus", login.USUARIO ,"!")
                break
            case 1:
                calculadora.calc()
            case 2:
                print("Aqui chamo calcula-frete!")
            case _:
                print("Opção invalida!\n") 
