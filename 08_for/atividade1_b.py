inicio = True
while inicio:
    try:
        numero = int(input("Digite um número inteiro: "))
        for multiplicador in range (1, 11):
            resultado = numero * multiplicador
            print("numero", "x", multiplicador, "=", resultado)
        inicio = False
    except ValueError:
        print("Por favor, digite um número inteiro válido.")