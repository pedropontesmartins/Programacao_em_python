try:
    nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
    nota2 = float(input("Digite a segunda nota: ").replace(",", "."))
    nota3 = float(input("Digite a terceira nota: ").replace(",", "."))
    media = (nota1 + nota2 + nota3) / 3
    print("A média das notas é:", media)
except ValueError:
    print("Por favor, digite valores válidos para as notas.")
