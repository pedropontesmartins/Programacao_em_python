import read 
while True:
  print("\n--- NOVO CADASTRO ---")
  nome = read.ler_texto("Digite seu nome completo: ")
  idade = read.ler_inteiro("Digite sua idade: ")
  peso = read.ler_float("Digite seu peso (kg): ")
  print("\n" + "=" * 40)
  print("         DADOS CADASTRADOS")
  print("=" * 40)
  print(f"Nome completo : {nome}")
  print(f"Idade         : {idade} anos")
  print(f"Peso          : {peso:.2f} kg")
  print("=" * 40 + "\n")
  continuar = read.ler_opcao(
      "Deseja realizar um novo cadastro? (S/N): "
  )
  if continuar == "N":
    print("\nEncerrando o programa. Até logo!")
    break
