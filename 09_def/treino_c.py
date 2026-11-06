start=True
def calcular_desconto(preco, desconto):
    preco_final = preco - (preco * (desconto / 100))
    return preco_final
while start:
    try:
        preco=float(input("Digite o preço do produto: ").replace(",","."))
        desconto=float(input("Digite o percentual de desconto: ").replace(",","."))
        resultado = calcular_desconto(preco, desconto)
        print("O preço final do produto com desconto é: ", resultado)
        start=False
    except ValueError:
        print("Por favor, digite apenas números")