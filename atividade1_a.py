start = True
while start:
    try:
        senha = int(input("insira sua senha: "))
        if senha == 1234:
            start= False  
            print("senha correta")
        else:
            print("senha incorreta por favor tente novamente")
    except ValueError:
        print("por favor insira apenas números")
print("fim do programa")                
  
    
