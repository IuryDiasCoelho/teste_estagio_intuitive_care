import requests
import os
#link dos arquivos
URLS_ZIP = {
    "1T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/1T2025.zip",
    "2T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/2T2025.zip",
    "3T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/3T2025.zip",
}
#função de baixar
def baixar_arquivo(nome_arquivo: str, url: str, pasta_destino: str):
    print(f"Baixando {nome_arquivo}...")
    resposta = requests.get(url)

    if resposta.status_code != 200:
        raise Exception(f"Erro ao baixar {nome_arquivo}")

    if "zip" not in resposta.headers.get("Content-Type", ""):
        raise Exception(f"{nome_arquivo} não é um ZIP válido")

    caminho = os.path.join(pasta_destino, nome_arquivo)

    with open(caminho, "wb") as arquivo:
        arquivo.write(resposta.content)

    print(f"{nome_arquivo} baixado com sucesso.")

#salvar na pasta ou criar uma pasta e salvar
if __name__ == "__main__":
    pasta_raw = "data/raw"
    os.makedirs(pasta_raw, exist_ok=True)

    for nome, url in URLS_ZIP.items():
        baixar_arquivo(nome, url, pasta_raw)
