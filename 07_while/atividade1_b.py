num1 = int(input("insira o numero: "))
contador = 1
while contador <= 10:
    print(num1, "x", contador, "=", num1 * contador)
    contador += 1
    if contador > 10:
        print("fim da tabuada")