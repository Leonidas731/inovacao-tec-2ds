# Programa para calcular a média de 4 números

# Etapa 1: Solicitar os 4 números via input
numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))
numero3 = float(input("Digite o 3º número: "))
numero4 = float(input("Digite o 4º número: "))

# Etapa 2: Armazenar os números em uma lista
numeros = [numero1, numero2, numero3, numero4]

# Etapa 3: Calcular a média
# Soma todos os números e divide pela quantidade (4)
soma = sum(numeros)
media = soma / len(numeros)

# Etapa 4: Exibir o resultado com duas casas decimais
# Usa formatação de string para exibir exatamente 2 casas decimais
print(f"A média dos números é: {media:.2f}")
