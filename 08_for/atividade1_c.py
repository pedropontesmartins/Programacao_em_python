resultado = 0
for adicao in range (1, 6):
        inicio = True 
        while inicio:
            try:
                numero = int(input("Digite um número inteiro: "))
                print("numero", adicao, "=", numero)
                adicao += 1
                resultado = numero + resultado
                inicio = False
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
print("O resultado da soma é:", resultado)                
           