import mod_msg
import mod_inputs
import menu_principal
USUARIO = "Pedro"
SENHA = "12345"
def valida_usuario(user):
    while True:
        usuario = mod_inputs.recebe_str("\033[33mDigite seu usuario: \033[0m")
        if len(usuario) >= 5:
            if user == usuario:
                break
            else:
                print("\033[31mUsuário incorreto!\033[0m\n")
        else:
            print("\033[31mO usuario deve conter ao menos 5 caracteres!\033[0m")
    return usuario
def valida_senha(senha1):
    while True:
        senha = mod_inputs.recebe_senha("\033[33mDigite sua senha: \033[0m")
        if senha == senha1:
            break
        else:
            print("\033[31mSenha invalida!\033[0m\n")
    return senha
def main():
    mod_msg.msg_login_ini()
    usuario_validado = valida_usuario(USUARIO)
    senha_valida = valida_senha(SENHA)
    print(f"\n\033[32m<<<<<<<<<<| Bem vindo {usuario_validado}! |>>>>>>>>>>\033[0m\n")
    menu_principal.recebe_opção()

 