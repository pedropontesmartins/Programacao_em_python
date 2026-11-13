import read 
import MOD
while True:
    print("\n--- Cálculo do Raio da Circunferência ---")
    circunferencia = read.ler_float("Digite o valor da circunferência (C): ")
    pi = 3.14 #valor aproximado
    raio = circunferencia / (2 * pi)
    print(f"O raio (r) da circunferência é: {raio:.2f}")
    
    # Pergunta se o usuário deseja continuar ou encerrar
    continuar = read.ler_opcao("\nDeseja realizar um novo cálculo? (S/N): ")
    if continuar != 'S':
        print("Programa finalizado.")
        break
