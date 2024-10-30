texto = input("indique um texto")
while "  " in texto:
    texto = texto.replace("  ", " ")  # substitui dois espaços consecutivos por um espaço
print(texto)  # Saída: Este é um exemplo com espaços duplos.
