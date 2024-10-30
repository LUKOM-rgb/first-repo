nomecompleto = input("O seu nome completo: ")

# Divide o nome completo em partes
shortname = nomecompleto.split(" ")

# Usa o loop `for` para percorrer as partes do nome
for i, nome in enumerate(shortname):
    if i == 0:
        print("Primeiro nome:", nome)
    elif i == len(shortname) - 1:
        print("Último nome:", nome)

    




