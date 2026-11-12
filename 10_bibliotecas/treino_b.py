start= True
import math
while start:
    try:
        num1 = int(input("Primeiro número: "))
        if num1 < 0:
            print("Erro: Não existe raiz quadrada real de número negativo. Tente novamente.\n")
            continue
        num2 = int(input("Segundo número: "))
        raiz = math.sqrt(num1)
        potencia = math.pow(num1, num2)
        print(f"Raiz quadrada: {raiz:.0f}")
        print(f"Potência: {potencia:.0f}")
        start= False
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros válidos.\n")
