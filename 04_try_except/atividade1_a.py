#recebendo dados 
try: 
    idade=int(input("Digite sua idade: "))
except ValueError:
    print("Por favor, digite um número válido.")