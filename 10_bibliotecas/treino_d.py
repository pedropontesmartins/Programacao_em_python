start= True
from datetime import date, timedelta
while start:
    try:
        hoje = date.today()
        prazo = input("Informe o prazo de entrega (em dias): ")
        prazo = int(prazo)
        saida = hoje + timedelta(days=prazo)
        print(f"Prazo estimado de entrega: {saida}")        
        start= False 
    except ValueError:
        print("Erro: Data inválida ou caractere incorreto. Verifique os valores e tente novamente.\n")
