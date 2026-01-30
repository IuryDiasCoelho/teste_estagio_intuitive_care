# Teste Técnico – Estágio em Tecnologia | Intuitive Care

## 📌 Objetivo
Este projeto foi desenvolvido como parte do **Teste de Entrada para Estagiários**, conforme especificado no documento **TESTE_ENTRADA_ESTAGIARIOS_v2.pdf**, com foco na **coleta, extração e consolidação de dados públicos da ANS** (Agência Nacional de Saúde Suplementar).

A implementação contempla integralmente a **Etapa 1 – Teste de API e Processamento de Dados**.

---

## 🗂️ Estrutura do Projeto

teste_estagio_intuitive_care/  
└── teste_1_api_dados/  
└── src/  
├── data/  
│ ├── raw/ # Arquivos ZIP originais baixados da ANS  
│ ├── processed/ # Arquivos CSV extraídos por trimestre  
│ └── final/ # Arquivo consolidado final   
│  
├── download_dados.py # Download dos arquivos ZIP  
├── extracao_zip.py # Extração automática dos arquivos  
├── processamento.py # Consolidação dos dados  
└── main.py # Orquestração do pipeline


---

## ✅ Etapa 1 – Teste de API e Processamento de Dados

### 1.1 Coleta de Dados
- Realizado o download automático dos arquivos ZIP trimestrais de 2025 disponibilizados pela ANS:
  - `1T2025.zip`
  - `2T2025.zip`
  - `3T2025.zip`
- Os arquivos são salvos na pasta `data/raw`.

---

### 1.2 Processamento de Arquivos
- Extração automática dos arquivos ZIP.
- Identificação e leitura dos arquivos CSV extraídos.
- Organização dos dados por trimestre na pasta `data/processed`.

**Trade-off técnico adotado:**
- O processamento foi feito de forma **incremental por arquivo**, tornando a solução mais eficiente e escalável.

---

### 1.3 Consolidação dos Dados
- Consolidação dos arquivos processados em um único arquivo.
- Geração do arquivo final:
  - `dados_consolidados.csv`
- Compactação do resultado final em:
  - `dados_consolidados.zip`, localizado em `data/final`.

---

## ▶️ Execução do Projeto

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Navegue até o diretório `src`.
3. Execute o pipeline completo com:

```bash
python main.py

O processo realiza automaticamente:

Download dos dados

Extração dos arquivos ZIP

Processamento dos CSVs

Consolidação final dos dados

🛠️ Tecnologias Utilizadas

Python

Bibliotecas padrão (os, zipfile, csv)

Organização de pipeline em etapas (ETL)

📌 Observações

As etapas de enriquecimento, agregação e análise fazem parte do escopo do teste e podem ser implementadas na sequência do projeto.

🔎 Limitações e Status do Projeto

A implementação deste projeto contempla integralmente a Etapa 1 – Teste de API e Processamento de Dados, conforme descrito no documento TESTE_ENTRADA_ESTAGIARIOS_v2.pdf.

As etapas subsequentes não foram concluídas para o teste. Apesar de a estrutura do projeto já prever essas fases, não foi possível avançar em sua implementação completa.

Ainda assim, optou-se por priorizar:
- A correta coleta, extração e consolidação dos dados
- A organização do pipeline e da estrutura do projeto
- A clareza e legibilidade do código entregue

👤 Autor

Iury Dias Coelho
Estudante de Engenharia de Software – 6º período Estacio de sa
Estudante de desenvolvimento Web Mobile- 1° período Escola do Futuro

🔗 LinkedIn:
https://www.linkedin.com/in/iury-dias-coelho-5009a6298/