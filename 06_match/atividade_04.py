valor = float(input("Digite o valor do produto: "))
print ("Escolha a categoria do produto:")
print ("1 - Informática")
print ("2 - Eletrônicos")
print ("3 - Acessórios")
desconto = int(input("Digite o número correspondente à categoria: "))
match desconto:
    case 1:
        print("Categoria escolhida: Informática desconto de 10% aplicado")
        valor = valor * (1 - 0.10)
        print("Valor com desconto: ", valor)
    case 2:
        print("Categoria escolhida: Eletrônicos desconto de 5% aplicado")
        valor = valor * (1 - 0.05)
        print("Valor com desconto: ", valor)
    case 3:
        print("Categoria escolhida: Acessórios desconto de 2% aplicado")
        valor = valor * (1 - 0.02)
        print("Valor com desconto: ", valor)
