
print("Escolha um número de 1 a 4 para escolher o problema correspondente:")
print (":")
print ("1 - computador não liga")
print ("2 - computador lento")
print ("3 - problema com a internet")
print ("4 - problema de impressão")
num1 = int(input("Digite o número: "))
if num1 < 1 or num1 > 4:
    print("Erro: O número deve estar entre 1 e 4.")
else:
    match num1:
        case 1:
            print("verifique se o cabo de energia está conectado corretamente e se a tomada está funcionando.")
        case 2:
            print("verifique se o computador está sobrecarregado e se há programas desnecessários rodando em segundo plano.")
        case 3:
            print("verifique se o roteador está funcionando corretamente e se há problemas com o provedor de internet.")
        case 4:
            print("verifique se a impressora está conectada corretamente e se há papel suficiente.")
    print("Deseja escolher outro problema? (s/n)")
    resposta = input().lower()
    if resposta == "s":
        print("Escolha um número de 1 a 4 para escolher o problema correspondente:")
        print ("1 - computador não liga")
        print ("2 - computador lento")
        print ("3 - problema com a internet")
        print ("4 - problema de impressão")
        num1 = int(input("Digite o número: "))
    else:
        print("Obrigado por utilizar o programa de suporte técnico.")
