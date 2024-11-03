listnumeros = []
listnome = []



for i in range(0,11):
    nome = str(input("Insira o nome do aluno:"))
    numero = int(input("Insira a sua nota:"))
    if  10 <= numero :
        listnumeros.append(numero)
        listnome.append(nome)
    else:
        continue



print(listnumeros)
print(listnome)