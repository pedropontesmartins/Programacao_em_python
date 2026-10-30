num1 = int(input("Digite o número: "))

if num1 < 1 or num1 > 7:
    print("Erro: O número deve estar entre 1 e 7.")
else:
    match num1:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")    
        case 7:
            print("Sábado")    