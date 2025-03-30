import os
import csv
import pandas as pd
import zipfile
import pdfplumber

# Caminhos
pdf_path = os.path.join("anexos", "Anexo_I.pdf")
csv_path = "Rol_de_Procedimentos.csv"
zip_path = "Teste_JoaoOtavio.zip"

# Lista para armazenar linhas
linhas_tabela = []

print("📄 Lendo PDF com pdfplumber...")
with pdfplumber.open(pdf_path) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                # ignora linhas completamente vazias
                if any(celula is not None and celula.strip() for celula in linha):
                    linhas_tabela.append(linha)

print(f"🔢 Total de linhas extraídas: {len(linhas_tabela)}")

# Salvar como CSV
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(linhas_tabela)

# Substituir abreviações (OD, AMB, HCO, HSO, REF) usando pandas
df = pd.read_csv(csv_path)
df.replace({
    "OD": "Odontologia",
    "AMB": "Ambulatorial",
    "HCO": "Seg. Hospitalar Com Obstetrícia",
    "HSO": "Seg. Hospitalar Sem Obstetrícia",
    "REF": "Plano Referência"
}, inplace=True)
df.to_csv(csv_path, index=False)

# Compactar em ZIP
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write(csv_path)

print(f"✅ CSV salvo como: {csv_path}")
print(f"📦 ZIP criado: {zip_path}")
