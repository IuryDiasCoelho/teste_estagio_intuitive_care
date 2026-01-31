import os
import zipfile
import requests

# link dos arquivos
URLS_ZIP = {
    "1T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/1T2025.zip",
    "2T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/2T2025.zip",
    "3T2025.zip": "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2025/3T2025.zip",
    "Relatorio_cadop.csv": "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv",
}

# função de baixar
def baixar_arquivo(nome_arquivo: str, url: str, pasta_destino: str, timeout: int = 60):
    print(f"Baixando {nome_arquivo}...")
    os.makedirs(pasta_destino, exist_ok=True)

    try:
        resposta = requests.get(url, stream=True, timeout=timeout)
        resposta.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Erro ao baixar {nome_arquivo} ({url}): {e}") from e

    caminho = os.path.join(pasta_destino, nome_arquivo)

    # Validação do tipo esperado pelo nome do arquivo (robusto para servidores que variam Content-Type)
    nome_lower = nome_arquivo.lower()
    esperado_zip = nome_lower.endswith(".zip")
    esperado_csv = nome_lower.endswith(".csv")

    if not (esperado_zip or esperado_csv):
        raise Exception(
            f"Extensão não suportada para {nome_arquivo}. "
            "Este downloader suporta apenas .zip e .csv."
        )

    # Se for ZIP, faça uma verificação rápida por assinatura antes de gravar tudo
    if esperado_zip:
        assinatura = resposta.raw.read(4, decode_content=True)
        if assinatura[:2] != b"PK":
            content_type = resposta.headers.get("Content-Type", "")
            raise Exception(
                f"{nome_arquivo} deveria ser ZIP, mas não parece um ZIP válido. "
                f"Content-Type recebido: {content_type!r}"
            )

        # Precisamos escrever também esses 4 bytes já lidos
        with open(caminho, "wb") as arquivo:
            arquivo.write(assinatura)
            for chunk in resposta.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    arquivo.write(chunk)

        # Confirmação final usando zipfile (validação real do arquivo)
        if not zipfile.is_zipfile(caminho):
            raise Exception(f"{nome_arquivo} foi baixado, mas o arquivo não é um ZIP válido/corrompido.")
    else:
        # CSV: apenas salva o conteúdo (sem exigir Content-Type específico)
        with open(caminho, "wb") as arquivo:
            for chunk in resposta.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    arquivo.write(chunk)

    print(f"{nome_arquivo} baixado com sucesso em: {caminho}")


# salvar na pasta ou criar uma pasta e salvar
if __name__ == "__main__":
    pasta_raw = "data/raw"
    os.makedirs(pasta_raw, exist_ok=True)

    for nome, url in URLS_ZIP.items():
        baixar_arquivo(nome, url, pasta_raw)