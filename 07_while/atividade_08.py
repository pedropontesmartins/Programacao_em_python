numero_secreto = 25
tentativas = 0
while True:
    palpite = int(input("Digite um número: "))
    tentativas += 1 
    if palpite > numero_secreto:
        print("O número secreto é menor!")
    elif palpite < numero_secreto:
        print("O número secreto é maior!")
    else:
        print("Parabéns! Você acertou!")
        break 
print("Foram necessárias: ", tentativas, "tentativas.")
