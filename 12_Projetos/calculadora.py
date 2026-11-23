import math
import mod_msg
import mod_inputs
import menu_principal
def calc():
    print("<<<<< CALCULADORA >>>>>")
    print("0 - sair")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - raiz")
    print("6 - potencia")
    print("7 - porcentagem")
    while True:

        opcao = input("\nEscolha uma operação: ")
        if opcao == "0":
            print("Voltando ao menu principal!")
            break
        if opcao in [ "1", "2", "3", "4", "5", "6", "7"]:
            if opcao != "5":
                num1 = float(input("Digite o primeiro numero: "))
                num2 = float(input("Digite o segundo numero: "))
            if opcao == "1":
                resultado = num1 + num2
                print("Resultado = ", resultado)
            elif opcao == "2":
                resultado = num1 - num2  
                print("Resultado =", resultado)  
            elif opcao == "3":
                resultado = num1 * num2
                print("Resultado = ", resultado)
            elif opcao == "4":
                    if num2 != 0:
                        resultado = num1 / num2                
                        print("Resultado = ", resultado)
                    else:
                        print("É impossivel dividir por zero")
            elif opcao == "5":
                        from math import sqrt
                        num1 = float(input("Digite seu numero: "))
                        resultado = math.sqrt(num1) 
                        print("Resultado = ", resultado)
            elif opcao == "6":
                from math import pow
                resultado = math.pow(num1, num2)
                print("Resultado = ", resultado)
            elif opcao == "7":
                resultado = num1*(num2/100)
                print("Resultado = ", resultado, "%")
        else:
            print("Operação invalida!")
