saldo = 1000.00
consultar = 1
depositar = 2
sacar = 3
sair = 4
match consultar:
    case 1:
        print("Seu saldo é: ", saldo)
    case 2:
        valor = float(input("Digite o valor a ser depositado: "))
        saldo += valor
        print("Depósito realizado com sucesso. Seu novo saldo é:", saldo)
    case 3:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor <= saldo:
            saldo -= valor
            print("Saque realizado com sucesso. Seu novo saldo é:", saldo)
        else:
            print("Saldo insuficiente.")
    case 4:
        print("Obrigado por usar nosso serviço.")
    case _:
        print("Opção inválida.")
