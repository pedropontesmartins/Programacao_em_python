#variaveis
potencia=float(input("Digite a potência do chuveiro (W): "))
voltagem=float(input("Digite a voltagem do chuveiro (V): "))
#calculo
amperagem=potencia/voltagem
disjuntor=amperagem * 1.10
#retorno
print("A amperagem calculada para o disjuntor (com 10% de margem) é:", round(disjuntor, 2), "A")
print("O disjuntor deve ser de no mínimo: ", round(disjuntor, 2), "A")
