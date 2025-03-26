import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# URL da página principal
URL_SITE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Criar pasta
PASTA = "anexos"
os.makedirs(PASTA, exist_ok=True)

print("🔎 Acessando a página principal da ANS...")
res = requests.get(URL_SITE)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

# Nomes exatos dos arquivos no href
TARGETS = {
    "Anexo_I.pdf": "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "Anexo_II.pdf": "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
}

# Buscar os links exatos pelos nomes dos arquivos
pdf_links = {}

for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    for nome_local, nome_arquivo in TARGETS.items():
        if nome_arquivo in href:
            pdf_links[nome_local] = (
                "https://www.gov.br" + href if not href.startswith("http") else href
            )

# Verificar se encontrou os dois
if len(pdf_links) != 2:
    print("❌ Links encontrados:")
    print(pdf_links)
    raise Exception("❌ Não foi possível encontrar os dois anexos na página.")

# Baixar os PDFs
caminhos_arquivos = []
for nome_arquivo, url in pdf_links.items():
    caminho = os.path.join(PASTA, nome_arquivo)
    print(f"⬇️ Baixando {nome_arquivo}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(caminho, 'wb') as f:
            f.write(response.content)
        caminhos_arquivos.append(caminho)
    except Exception as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")

# Compactar os PDFs
zip_path = os.path.join(PASTA, "anexos_compactados.zip")
with ZipFile(zip_path, 'w') as zipf:
    for caminho in caminhos_arquivos:
        zipf.write(caminho, os.path.basename(caminho))

print(f"\n✅ PDFs salvos em '{PASTA}/'")
print(f"📦 ZIP criado em: {zip_path}")
