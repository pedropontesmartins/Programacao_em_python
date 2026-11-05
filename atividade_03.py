num = int(input("Digite um numero inteiro: "))
tabuada = 1 
while tabuada <=10:
    resultado = num * tabuada
    print(num, "X", tabuada, "=", resultado)
    tabuada += 1 
    if tabuada > 10:
        print("tabuada finalizada")
         

