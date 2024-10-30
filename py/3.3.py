nome = input("Indique um nome: ")

comp = len(nome)
nome2 = ""

for i in range(comp-1,-1,-1):
    print(nome[i], end="")
    nome2 += nome[i] 


if nome == nome2:
        print(f"A palavra {nome} é uma capicua ")
else:
        print(f"A palavra {nome} não é uma capicua")