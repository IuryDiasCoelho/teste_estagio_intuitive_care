import os
import zipfile
import pandas as pd


def processar_dados(pasta_processed: str, arquivo_saida: str):

    # Lê todos os documentos e junta em um único arquivo.

    dataframes = []

    for pasta in os.listdir(pasta_processed):
        caminho_pasta = os.path.join(pasta_processed, pasta)

        if os.path.isdir(caminho_pasta):
            for arquivo in os.listdir(caminho_pasta):
                if arquivo.endswith(".csv"):
                    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
                    print(f"Lendo {caminho_arquivo}")

                    df = pd.read_csv(caminho_arquivo, sep=";", encoding="latin1")
                    df["trimestre"] = pasta
                    dataframes.append(df)

    if not dataframes:
        raise FileNotFoundError(
            f"Nenhum arquivo .csv encontrado em subpastas de: {pasta_processed}"
        )

    df_final = pd.concat(dataframes, ignore_index=True)

    pasta_saida = os.path.dirname(arquivo_saida) or "."
    os.makedirs(pasta_saida, exist_ok=True)

    caminho_zip = os.path.join(pasta_saida, "dados_consolidados.zip")

    # Gera o CSV em memória e grava direto no ZIP (não cria .csv no disco)
    csv_texto = df_final.to_csv(index=False)
    csv_bytes = csv_texto.encode("utf-8-sig")

    with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr("dados_consolidados.csv", csv_bytes)

    print("Dados processados e consolidados com sucesso.")
    print(f"ZIP final: {caminho_zip}")


if __name__ == "__main__":
    pasta_processed = "data/processed"
    pasta_saida = "data/final"

    os.makedirs(pasta_saida, exist_ok=True)

    arquivo_saida = os.path.join(pasta_saida, "dados_consolidados.csv")
    processar_dados(pasta_processed, arquivo_saida)