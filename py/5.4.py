def criar_matriz(linhas, colunas):
    """Permite ao usuário criar uma matriz preenchendo-a manualmente."""
    print(f"Digite os elementos da matriz ({linhas}x{colunas}):")
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz1, matriz2):
    """Soma duas matrizes de mesma ordem."""
    linhas, colunas = len(matriz1), len(matriz1[0])
    return [[matriz1[i][j] + matriz2[i][j] for j in range(colunas)] for i in range(linhas)]

def subtrair_matrizes(matriz1, matriz2):
    """Subtrai duas matrizes de mesma ordem."""
    linhas, colunas = len(matriz1), len(matriz1[0])
    return [[matriz1[i][j] - matriz2[i][j] for j in range(colunas)] for i in range(linhas)]

def exibir_matriz(matriz):
    """Exibe a matriz de forma estruturada."""
    for linha in matriz:
        print(" ".join(map(str, linha)))

def menu():
    """Menu principal do programa."""
    while True:
        print("\nMENU")
        print("1 - Somar matrizes")
        print("2 - Subtrair matrizes")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao in ["1", "2"]:
            linhas = int(input("Digite o número de linhas das matrizes: "))
            colunas = int(input("Digite o número de colunas das matrizes: "))
            
            print("\nMatriz 1:")
            matriz1 = criar_matriz(linhas, colunas)
            
            print("\nMatriz 2:")
            matriz2 = criar_matriz(linhas, colunas)

            if opcao == "1":
                print("\nResultado da Soma:")
                resultado = somar_matrizes(matriz1, matriz2)
                exibir_matriz(resultado)
            elif opcao == "2":
                print("\nResultado da Subtração:")
                resultado = subtrair_matrizes(matriz1, matriz2)
                exibir_matriz(resultado)
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menu()
