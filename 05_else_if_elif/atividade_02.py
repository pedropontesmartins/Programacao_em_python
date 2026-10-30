nota= float(input("Digite a nota do aluno: "))
if nota < 0 or nota > 10:
    print("Nota inválida")
elif nota >0 and nota <4.9:
    print("Reprovado")
elif nota >5 and nota <6.9:
    print("Recuperação")
else:
    print("Aprovado")