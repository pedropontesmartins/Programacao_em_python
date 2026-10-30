valor = float(input("digite o valor da compra: "))
if valor < 0:
    print("Valor inválido")
elif valor > 0 and valor < 99.99:
    print("sem desconto)")
elif valor > 100 and valor < 499.99:
    print("desconto de 10%")
elif valor > 500:
    print("desconto de 15%")