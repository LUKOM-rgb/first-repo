def inicializar_parque():
    """Inicializa o parque de estacionamento com todos os lugares livres."""
    return [[0 for _ in range(5)] for _ in range(3)]  # 0 indica lugar livre

def mostrar_estado_parque(parque):
    """Mostra o estado do parque: número de lugares ocupados e livres."""
    ocupados = sum(sum(fila) for fila in parque)
    livres = 15 - ocupados
    print(f"\nEstado do Parque:")
    print(f"Lugares ocupados: {ocupados}")
    print(f"Lugares livres: {livres}")

def entrada_veiculo(parque):
    """Ocupação do primeiro lugar livre no parque."""
    for i, fila in enumerate(parque):
        for j, lugar in enumerate(fila):
            if lugar == 0:  # Encontrar o primeiro lugar livre
                parque[i][j] = 1  # Marca como ocupado
                print(f"Veículo estacionado na posição: Fila {i+1}, Lugar {j+1}")
                return
    print("Parque completo! Não há lugares disponíveis.")

def saida_veiculo(parque):
    """Libera um lugar ocupado no parque."""
    try:
        fila = int(input("Digite a fila do veículo (1-3): ")) - 1
        lugar = int(input("Digite o lugar do veículo (1-5): ")) - 1
        if 0 <= fila < 3 and 0 <= lugar < 5:
            if parque[fila][lugar] == 1:
                parque[fila][lugar] = 0  # Libera o lugar
                print(f"Veículo removido da posição: Fila {fila+1}, Lugar {lugar+1}")
            else:
                print("Este lugar já está livre!")
        else:
            print("Posição inválida!")
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números válidos.")

def exibir_parque(parque):
    """Exibe o estado atual do parque de estacionamento."""
    print("\nParque de Estacionamento (0: Livre, 1: Ocupado):")
    for i, fila in enumerate(parque):
        print(f"Fila {i+1}: {fila}")

def menu():
    """Menu principal do programa."""
    parque = inicializar_parque()
    while True:
        print("\nMENU")
        print("1 - Entrada de veículo")
        print("2 - Saída de carro")
        print("3 - Estado do Parque")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            entrada_veiculo(parque)
        elif opcao == "2":
            saida_veiculo(parque)
        elif opcao == "3":
            exibir_parque(parque)
            mostrar_estado_parque(parque)
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menu()
