import read 
while True:
    print("\n--- Calculadora ---")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    operacao = input("Escolha o número da operação desejada: ")
    if operacao not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
        continue
    try:
        num1 = read.ler_float("Digite o primeiro número: ")
        num2 = read.ler_float("Digite o segundo número: ")
    except ValueError:
        print("Erro! Por favor, digite apenas valores numéricos.")
        continue
    if operacao == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacao == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif operacao == '4':
        if num2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
    continuar = input("\nDeseja realizar um novo cálculo? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa finalizado.")
        break
