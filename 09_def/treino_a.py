start = True
def calcular_soma(num1, num2):    
    soma = num1 + num2
    return soma
while start:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = calcular_soma(n1, n2)
        print("A soma dos números é: ", resultado)
        start = False
    except ValueError:
        print("Por favor, digite apenas números inteiros.")