import read
import MOD 
start = True 
def classificar_imc(imc, idade):
    if idade > 60:
        if imc < 22:
            return "Baixo peso"
        elif imc <= 27:
            return "Adequado ou eutrófico"
        else:
            return "Sobrepeso"
    else:
        if imc < 18.5:
            return "Baixo peso"
        elif imc < 25:
            return "Normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"
def main():
    print("=== CALCULADORA DE IMC - USO OFFLINE ===")
    while True:
        print("\n--- Dados do Paciente ---")
        nome = input("Nome do cliente: ").strip()
        try:
            idade = int(input("Idade (anos): "))
            peso = float(input("Peso (kg): ").replace(",", "."))
            altura = float(input("Altura (m): ").replace(",", "."))
            if altura <= 0 or peso <= 0 or idade < 0:
                print("\nErro: Os valores de idade, peso e altura devem ser maiores que zero.")
                continue
        except ValueError:
            print("\nErro: Por favor, digite apenas números válidos para idade, peso e altura.")
            continue
        imc = peso / (altura ** 2)
        classificacao = classificar_imc(imc, idade)
        print("\n" + "=" * 35)
        print("RESULTADO DA AVALIAÇÃO")
        print("=" * 35)
        print(f"Nome:          {nome}")
        print(f"Idade:         {idade} anos")
        print(f"Peso:          {peso:.2f} kg")
        print(f"Valor do IMC:  {imc:.2f} kg/m²")
        print(f"Classificação: {classificacao}")
        print("=" * 35)
        continuar = input("\nDeseja realizar um novo cálculo? (S/N): ").strip().upper()
        if continuar != "S":
            print("\nPrograma finalizado. Até logo!")
            break
if __name__ == "__main__":
    main()
