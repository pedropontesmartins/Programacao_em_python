start= True
from datetime import date
while start:
    try:
        ano = int(input("Ano de nascimento (ex: 1995): "))
        mes = int(input("Mês de nascimento (1 a 12): "))
        dia = int(input("Dia de nascimento (1 a 31): "))
        nascimento = date(ano, mes, dia)
        hoje = date.today()
        if nascimento > hoje:
            print("Erro: A data de nascimento não pode ser no futuro. Tente novamente.\n")
            continue
        idade = hoje.year - nascimento.year
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1
        print(f"Idade do funcionário: {idade} anos completos.")        
        start= False 
    except ValueError:
        print("Erro: Data inválida ou caractere incorreto. Verifique os valores e tente novamente.\n")
