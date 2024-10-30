def reverseWords(texto):
    # Divide o texto em palavras
    palavras = texto.split()
    
    # Inverte a lista de palavras
    palavras_invertidas = palavras[::-1]
    
    # Junta as palavras em uma única string
    texto_invertido = ' '.join(palavras_invertidas)
    
    return texto_invertido

# Exemplo de uso
texto = "Isto é um exemplo de texto"
resultado = reverseWords(texto)
print(resultado)  # Saída: "texto de exemplo um é Isto"
