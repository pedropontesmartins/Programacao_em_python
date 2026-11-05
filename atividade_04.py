soma_total = 0
contador = 0
while contador < 5:
    numero = int(input("Digite o " + str(contador + 1) + "º número inteiro: "))
    soma_total += numero
    contador += 1
print("A soma total dos números informados é: ", soma_total)
