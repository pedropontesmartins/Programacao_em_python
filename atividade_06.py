soma_notas = 0.0
contador_notas = 0
print("Digite as notas do aluno (ou -1 para encerrar e calcular):")
nota = float(input("Digite uma nota: "))
while nota != -1:
    soma_notas += nota
    contador_notas += 1
    nota = float(input("Digite uma nota: "))
if contador_notas > 0:
    media = soma_notas / contador_notas
    print("\nQuantidade de notas informadas:", contador_notas)
    print(f"Média das notas:  {media:.2f}")
else:
    print("\nNenhuma nota válida foi informada.")

