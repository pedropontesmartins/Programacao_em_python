start=True
def verificar_numero(numero):
    if numero % 2 == 0:
        return "O numero é par."
    else:
        return "O numero é impar."  

while start:
    try:
        n1 = int(input("Digite um numero: "))        
        resultado = verificar_numero(n1)
        print(resultado)
        start=False
    except ValueError:
        print("Por favor, digite apenas números")

