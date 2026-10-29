try:
    preço= int(input("digite o preço do produto: "))
    desconto= int(input("digite o desconto aplicado: "))
    preço_final = preço - (preço * desconto/100)
    print("O preço final do produto é:", preço_final)
except ValueError:
    print("Por favor, digite um valor válido para o preço e o desconto.")