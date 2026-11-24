import mod_msg
import mod_inputs
import calculadora
import login
import calc_frete
def recebe_opção():
    while True:
        mod_msg.msg_menu_pricipal()
        opcao =mod_inputs.recebe_int("Insira sua opção - ")
        match opcao:
            case 0:
                print(f"\033[31m<<<<<<<<<<| Adeus {login.USUARIO}! |>>>>>>>>>>\033[0m\n")
                break
            case 1:
                calculadora.calc()
            case 2:
                calc_frete.executar()
            case _:
                print("\033[31mOpção invalida!\033[0m\n") 
                
