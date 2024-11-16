def invert(matriz):
    # Imprime a matriz original
    print("Matriz Original:")
    for linha in matriz:
        print(linha)
    
    # Calcula e imprime a transposta da matriz
    print("\nMatriz Transposta:")
    for i in range(3):
        transposta = [matriz[j][i] for j in range(3)]
        print(transposta)

# Função para ler a matriz 3x3
def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            num = int(input(f"Elemento [{i+1}][{j+1}]: "))
            linha.append(num)
        matriz.append(linha)
    return matriz

# Main
matriz = ler_matriz()
invert(matriz)
