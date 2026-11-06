start = True 
def calcular_media(num1, num2, num3):
    media = (num1 + num2+ num3 )/3
    return media 
while start:
    try:
        n1=float(input("Digite o primeiro número: ")).replace(",",".")
        n2=float(input("Digite o segundo número: ")).replace(",",".")
        n3=float(input("Digite o terceiro número: ")).replace(",",".")
        resultado = calcular_media(n1, n2, n3)
        print("A média do aluno é: ", resultado)
        start=False
    except ValueError:
        print("Por favor, digite apenas números")

        