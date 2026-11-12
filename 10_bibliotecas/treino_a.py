start= True
import math
while True:
    try:
        entrada = input("Digite o raio da mesa: ").replace(",", ".")
        raio = float(entrada)
        area = math.pi * (raio ** 2)
        print(f"A área da mesa circular é: {area:.2f}")
        start= False
    except ValueError:
        print("Erro: Por favor, digite apenas números.")
