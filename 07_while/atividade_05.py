try:
    print("Bem vindo usuario, para acessar o sistema digite a senha correta")
    senha_correta = 12345
    senha_digitada = int(input("digite a senha:"))
    while senha_digitada != senha_correta:
        print("senha incorreta, tente novamente")
        senha_digitada = int(input("digite a senha: "))
except ValueError:
    print("entrada invalida. por favor, insira um numero inteiro.")
print("senha correta, acesso liberado!")