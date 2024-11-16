from PIL import Image, ImageOps
import os

def imageMoldura(caminho_imagem):
    try:
        # Abre a imagem fornecida
        imagem = Image.open(caminho_imagem)

        # Define a largura da moldura
        largura_moldura = 20

        # Cria a moldura usando ImageOps.expand
        imagem_com_moldura = ImageOps.expand(imagem, border=largura_moldura, fill="magenta")

        # Mostra a imagem com a moldura
        imagem_com_moldura.show()

        # Cria a sub-pasta "images" e salva a imagem com moldura
        pasta_saida = "images"
        os.makedirs(pasta_saida, exist_ok=True)
        caminho_saida = os.path.join(pasta_saida, "imagem_com_moldura.jpg")
        imagem_com_moldura.save(caminho_saida)

        print(f"A imagem com moldura foi salva em: {caminho_saida}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_imagem} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de chamada da função
# Substitua 'caminho_da_imagem.jpg' pelo caminho de uma imagem válida
caminho_da_imagem = "images/bandeira.jpg"  # Atualize com o caminho correto
imageMoldura(caminho_da_imagem)
