def ler_texto(mensagem):
  while True:
    valor = input(mensagem).strip()
    if valor and all(parte.isalpha() for parte in valor.split()):
      return valor.title()
    print("Erro: Digite um nome válido (apenas letras, sem ficar em branco).")
def ler_inteiro(mensagem):
  while True:
    try:
      valor = int(input(mensagem))
      if valor >= 0:
        return valor
      print("Erro: O número não pode ser negativo.")
    except ValueError:
      print("Erro: Digite apenas números inteiros válidos.")
def ler_float(mensagem):
  while True:
    try:
      entrada = input(mensagem).strip().replace(",", ".")
      valor = float(entrada)
      if valor > 0:
        return valor
      print("Erro: O valor deve ser maior que zero.")
    except ValueError:
      print("Erro: Digite um valor numérico válido (ex: 70.5 ou 70,5).")
def ler_opcao(mensagem):
  while True:
    opcao = input(mensagem).strip().upper()
    if opcao in ["S", "N"]:
      return opcao
    print("Erro: Opção inválida. Digite apenas S ou N.")
