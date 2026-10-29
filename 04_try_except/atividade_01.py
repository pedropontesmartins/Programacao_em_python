try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Por favor, digite um valor válido para a idade.")    
try:
    nome = str(input("Digite seu nome: "))
except ValueError:
    print("Por favor, digite um valor válido para o nome.")
print(f"Olá", nome,"!", "Você tem",idade, "anos.")