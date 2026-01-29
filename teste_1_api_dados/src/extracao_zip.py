import zipfile
import os

def extrair_zip(caminho_zip: str, pasta_destino: str):
    """
    Extrai um arquivo ZIP para a pasta de destino.
    """
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)
        print(f"Extraído: {os.path.basename(caminho_zip)}")


if __name__ == "__main__":
    pasta_raw = "data/raw"
    pasta_processed = "data/processed"

    os.makedirs(pasta_processed, exist_ok=True)

    for arquivo in os.listdir(pasta_raw):
        if arquivo.endswith(".zip"):
            caminho_zip = os.path.join(pasta_raw, arquivo)

            nome_pasta = arquivo.replace(".zip", "")
            destino = os.path.join(pasta_processed, nome_pasta)

            os.makedirs(destino, exist_ok=True)

            extrair_zip(caminho_zip, destino)

    print("Todos os arquivos ZIP foram extraídos com sucesso.")
