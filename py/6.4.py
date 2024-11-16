from PIL import Image
import os

def imageGrayScale(caminho_imagem):
    try:
        # Abre a imagem fornecida
        imagem = Image.open(caminho_imagem)
        
        # Converte a imagem para RGB caso não esteja neste modo
        imagem = imagem.convert("RGB")

        # Obtem os pixels da imagem original
        largura, altura = imagem.size
        nova_imagem = Image.new("L", (largura, altura))  # Cria uma imagem GrayScale (modo "L")
        pixels_original = imagem.load()
        pixels_novo = nova_imagem.load()

        # Aplica a fórmula NTSC para cada pixel
        for x in range(largura):
            for y in range(altura):
                red, green, blue = pixels_original[x, y]
                gray = int(0.299 * red + 0.587 * green + 0.114 * blue)
                pixels_novo[x, y] = gray

        # Mostra a nova imagem em GrayScale
        nova_imagem.show()

        # Cria a sub-pasta "images" e salva a nova imagem
        pasta_saida = "images"
        os.makedirs(pasta_saida, exist_ok=True)
        caminho_saida = os.path.join(pasta_saida, "imagem_grayScale.jpg")
        nova_imagem.save(caminho_saida)

        print(f"A imagem em GrayScale foi salva em: {caminho_saida}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_imagem} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de chamada da função
# Substitua 'caminho_da_imagem.jpg' pelo caminho de uma imagem válida
caminho_da_imagem = "images/bandeira.jpg"  # Atualize com o caminho correto
imageGrayScale(caminho_da_imagem)
