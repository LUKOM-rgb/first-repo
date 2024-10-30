def printCharLine(texto, numeroCar):
    # Divide o texto em palavras
    palavras = texto.split()
    
    linha_atual = ""
    
    for palavra in palavras:
        # Se a linha atual mais a nova palavra exceder o limite, imprima a linha atual e reinicie
        if len(linha_atual) + len(palavra) + 1 > numeroCar:
            print(linha_atual.strip())  # Imprime a linha atual sem espaços extras
            linha_atual = palavra + " "  # Começa uma nova linha com a nova palavra
        else:
            linha_atual += palavra + " "  # Adiciona a palavra à linha atual

    # Imprime a última linha se não estiver vazia
    if linha_atual:
        print(linha_atual.strip())  # Imprime a última linha

# Exemplo de uso
texto = "Esta é uma função que imprime o texto em linhas com um número específico de caracteres."
numeroCar = 20
printCharLine(texto, numeroCar)
