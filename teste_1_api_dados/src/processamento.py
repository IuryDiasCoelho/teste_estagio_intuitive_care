import os
import zipfile
import pandas as pd


def processar_dados(pasta_processed: str, arquivo_saida: str):

#Lê todos os documentos e junta em um único arquivo.

    dataframes = []

    for pasta in os.listdir(pasta_processed):
        caminho_pasta = os.path.join(pasta_processed, pasta)

        if os.path.isdir(caminho_pasta):
            for arquivo in os.listdir(caminho_pasta):
                if arquivo.endswith(".csv"):
                    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
                    print(f"Lendo {caminho_arquivo}")

                    df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1')
                    df["trimestre"] = pasta
                    dataframes.append(df)

    df_final = pd.concat(dataframes, ignore_index=True)
    df_final.to_csv(arquivo_saida, index=False)


    os.makedirs(pasta_saida, exist_ok=True)

    caminho_csv_temp = os.path.join(pasta_saida, "dados_consolidados.csv")
    caminho_zip = os.path.join(pasta_saida, "dados_consolidados.zip")

    # Salva lista temporário
    df_final.to_csv(caminho_csv_temp, index=False)

    # Compacta
    with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(caminho_csv_temp, arcname="dados_consolidados.csv")

    # Remove lista temporário
    os.remove(caminho_csv_temp)

    print("Dados processados e consolidados com sucesso.")


if __name__ == "__main__":
    pasta_processed = "data/processed"
    pasta_saida = "data/final"

    os.makedirs(pasta_saida, exist_ok=True)

    arquivo_saida = os.path.join(pasta_saida, "dados_consolidados.csv")

    processar_dados(pasta_processed, arquivo_saida)
