from PIL import Image
import os

def criar_bandeira_vertical():
    # Dimensões da imagem
    largura, altura = 240, 240

    # Cria uma nova imagem RGB
    imagem = Image.new("RGB", (largura, altura))
    pixels = imagem.load()

    # Define as cores das faixas
    cores = [(0, 0, 255),  # Azul
             (255, 255, 255),  # Branco
             (255, 0, 0)]  # Vermelho

    # Preenche a imagem com as faixas verticais
    for x in range(largura):
        faixa = x // 80  # Determina a faixa (0, 1 ou 2)
        cor = cores[faixa]
        for y in range(altura):
            pixels[x, y] = cor

    # Cria a sub-pasta "images" se não existir e salva a imagem
    pasta_saida = "images"
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_saida, "bandeira.jpg")
    imagem.save(caminho_arquivo)

    print(f"A imagem da bandeira foi salva em: {caminho_arquivo}")

# Chama a função para criar e salvar a imagem
criar_bandeira_vertical()
