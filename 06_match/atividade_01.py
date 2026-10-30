num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operação = input("Digite a operação (+, -, *, /): ")

match operação:
    case "+":
        print(f"O resultado de {num1} {operação} {num2} é: {num1 + num2}") 
    case "-":
        print(f"O resultado de {num1} {operação} {num2} é: {num1 - num2}")
    case "*":
        print(f"O resultado de {num1} {operação} {num2} é: {num1 * num2}")  
    case "/":
        if num2 != 0:
            print(f"O resultado de {num1} {operação} {num2} é: {num1 / num2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
