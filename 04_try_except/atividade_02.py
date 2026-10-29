#variaveis e except
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma de",num1, "+", num2, "é:", resultado)
except ValueError: 
    print("Por favor, digite um número válido.")