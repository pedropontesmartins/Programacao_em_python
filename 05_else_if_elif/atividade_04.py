temperatura = float(input("Digite a temperatura em Celsius: "))
if temperatura < 0:
    print("congelante")
elif temperatura <= 15:
    print("frio")
elif temperatura > 15 and temperatura <=30:
    print("agradável")
elif temperatura >30: 
    print("muito quente")