from download_dados import baixar_arquivo
from extracao_zip import extrair_zip
from processamento import processar_dados
import os

URLS_ZIP = {
    "1T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/1T2025.zip",
    "2T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/2T2025.zip",
    "3T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/3T2025.zip",
}

def executar_pipeline():
    pasta_raw = "data/raw"
    pasta_processed = "data/processed"
    pasta_final = "data/final"

    os.makedirs(pasta_raw, exist_ok=True)
    os.makedirs(pasta_processed, exist_ok=True)
    os.makedirs(pasta_final, exist_ok=True)

    # baixar
    for nome, url in URLS_ZIP.items():
        caminho = os.path.join(pasta_raw, nome)
        baixar_arquivo(nome, url, pasta_raw)

    # extrair
    for arquivo in os.listdir(pasta_raw):
        if arquivo.endswith(".zip"):
            caminho_zip = os.path.join(pasta_raw, arquivo)
            destino = os.path.join(pasta_processed, arquivo.replace(".zip", ""))
            os.makedirs(destino, exist_ok=True)
            extrair_zip(caminho_zip, destino)

    # juntar arquivos
    arquivo_saida = os.path.join(pasta_final, "dados_consolidados.csv")
    processar_dados(pasta_processed, arquivo_saida)


if __name__ == "__main__":
    executar_pipeline()
