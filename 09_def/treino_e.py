start=True
def verificar_estoque(produto,quantidade):
    if quantidade <=5:
        return "O estoque está critico"
    if quantidade > 5 and quantidade <= 20:
        return "O estoque está baixo"
    if quantidade > 20:
        return "O estoque está adequado"
    else:
        return "Produto não encontrado"
nome_produto = input("Digite o nome do produto: ")    
while start:
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        if quantidade < 0:
            print("A quantidade não pode ser negativa")
            continue
        resultado = verificar_estoque(nome_produto,quantidade)
        print(resultado)
        start=False
    except ValueError:
        print("Por favor, digite apenas números")

