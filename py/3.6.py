nomecompleto = input("O seu nome completo: ")

# Divide o nome completo em partes
shortname = nomecompleto.split(" ")
nomesmeio = shortname[1:-1]
letras_maiusculas = []


# Usa o loop `for` para percorrer as partes do nome
for i, nome in enumerate(shortname):
    if i == 0:
        print("Primeiro nome:", nome)
    elif i == len(shortname) - 1:
        print("Último nome:", nome)
       
        
# Percorre cada letra no nome completo
for letra in nomecompleto:
    if letra.isupper():  # Verifica se a letra é maiúscula
        letras_maiusculas.append(letra)

print("Letras maiúsculas:", "".join(letras_maiusculas))



