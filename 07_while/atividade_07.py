saldo = 1000.00
while True:
    print("\n--- CAIXA ELETRÔNICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinheiro")
    print("3. Sacar dinheiro")
    print("4. Sair")
    opcao = input("Escolha uma opção (1-4): ")
    if opcao == '1':
        print("Seu saldo atual é: R$ ", saldo)
    elif opcao == '2':
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito 
            print("Depósito de R$ ",valor_deposito, "realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")
    elif opcao == '3':
        valor_saque = float(input("Digite o valor do saque: R$ "))
        if valor_saque > 0:
            if valor_saque <= saldo:
                saldo -= valor_saque  
                print("Saque de R$", valor_saque, "realizado com sucesso!")
            else:
                print("Saldo insuficiente para realizar este saque.")
        else:
            print("Valor de saque inválido.")
    elif opcao == '4':
        print("Encerrando o programa. Obrigado por utilizar o caixa eletrônico!")
        break
    else:
        print("Opção inválida. Tente novamente.")
