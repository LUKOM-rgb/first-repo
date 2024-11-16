from PIL import Image
import os
import random

def ImageArt():
    # Dimensões da imagem
    largura, altura = 400, 400

    # Cria uma nova imagem RGB
    imagem = Image.new("RGB", (largura, altura))
    pixels = imagem.load()

    # Preenche a imagem com valores RGB aleatórios
    for x in range(largura):
        for y in range(altura):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            pixels[x, y] = (red, green, blue)

    # Exibe a imagem
    imagem.show()

    # Cria a sub-pasta "images" se não existir e salva a imagem
    pasta_saida = "images"
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_saida, "imageArt.jpg")
    imagem.save(caminho_arquivo)

    print(f"A imagem foi salva em: {caminho_arquivo}")

# Chama a função para criar e salvar a imagem
ImageArt()
