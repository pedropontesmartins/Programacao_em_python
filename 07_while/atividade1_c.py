stay = True 
try:
    while stay:
        print("1-Cadastro")
        print("2-Consulta")
        print("3-Relatorio")
        print("4-Sair")
        escolha = int(input("insira sua escolha: "))
        if escolha == 4:
            stay = False
            print("fim do programa")
except ValueError:
    print("entrada invalida. por favor, insira um numero.")
    escolha = int(input("insira sua escolha: "))
    if escolha == 4:
        stay = False
        print("fim do programa")
    
