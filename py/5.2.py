import random

# Função para gerar uma matriz com valores aleatórios entre 10 e 100
def inicializar_matriz(linhas, colunas):
    matriz = [[random.randint(10, 100) for _ in range(colunas)] for _ in range(linhas)]
    print("\nMatriz Gerada:")
    for linha in matriz:
        print(linha)
    return matriz

# Função para calcular e imprimir a transposta da matriz
def matriz_transposta(matriz):
    print("\nMatriz Transposta:")
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    for linha in transposta:
        print(linha)

# Função para encontrar e imprimir o maior valor da matriz
def maior_valor(matriz):
    maior = max(max(linha) for linha in matriz)
    print(f"\nMaior valor na matriz: {maior}")

# Função principal do programa
def main():
    matriz = None
    while True:
        print("\nMenu:")
        print("1 - Inicializar matriz")
        print("2 - Matriz transposta")
        print("3 - Maior valor")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            linhas = int(input("Digite o número de linhas: "))
            colunas = int(input("Digite o número de colunas: "))
            matriz = inicializar_matriz(linhas, colunas)
        
        elif opcao == "2":
            if matriz is not None:
                matriz_transposta(matriz)
            else:
                print("A matriz ainda não foi inicializada!")
        
        elif opcao == "3":
            if matriz is not None:
                maior_valor(matriz)
            else:
                print("A matriz ainda não foi inicializada!")
        
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
