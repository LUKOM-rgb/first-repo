#40240224 Lucas Silva
cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']

lista = []

for i in range(len(cidades)):
    while True:
        try:
            temperatura = int(input(f"Coloque a temperatura de {cidades[i]} (entre 0 e 40): "))
            if 0 <= temperatura <= 40:
                lista.append(temperatura)
                break
            else:
                print("Erro: A temperatura deve estar entre 0 e 40.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

media = sum(lista) / len(cidades)

def dadosEstatistica(lista, media):
    listaNova = []

    for i in lista:
        listaNova.append(abs(media - i))

    indice_mais_distante = listaNova.index(min(listaNova))
    valor_mais_proximo = lista[indice_mais_distante]

    print("O valor mais próximo da média de temperatura é: {:.2f}".format(valor_mais_proximo))

dadosEstatistica(lista, media)
