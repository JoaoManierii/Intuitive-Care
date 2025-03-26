# 🔎 Download e Compactação dos Anexos da ANS (Rol de Procedimentos)

Este script em Python realiza automaticamente o download dos **Anexos I e II** disponibilizados no site oficial da **ANS (Agência Nacional de Saúde Suplementar)** e os salva em uma pasta local, além de criar um arquivo `.zip` contendo os dois PDFs.

---

## 📌 O que o script faz?

1. Acessa a página oficial da ANS com a lista de procedimentos atualizada:
   - [`https://www.gov.br/ans/.../atualizacao-do-rol-de-procedimentos`](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
2. Localiza os arquivos PDF exatos dos **Anexo I** e **Anexo II**, com base nos nomes reais dos arquivos.
3. Baixa os arquivos e salva na pasta `anexos/`.
4. Cria um arquivo `anexos_compactados.zip` na mesma pasta contendo os dois PDFs.

---

## 🛠️ Requisitos

- Python 3.7+
- Bibliotecas:
  - `requests`
  - `beautifulsoup4`

Para instalar as dependências:

```bash
pip install requests beautifulsoup4
```

## ▶️ Como usar
- Baixe ou copie o script Python para um arquivo, por exemplo: ex1.py
- No terminal ou PowerShell, execute:

```bash
python ex1.py
```
- Após a execução, será criada a seguinte estrutura:

``` python
📁 anexos/
├── Anexo_I.pdf
├── Anexo_II.pdf
└── anexos_compactados.zip
```

## 📦 Estrutura do Projeto

``` python
.
├── ex1.py                 
└── anexos/                
    ├── Anexo_I.pdf
    ├── Anexo_II.pdf
    └── anexos_compactados.zip
```

## 💡 Extras Técnicos

- O script usa BeautifulSoup para navegar no HTML da página.

- Os PDFs são localizados com base nos nomes reais dos arquivos, garantindo confiabilidade.

- Links relativos são corrigidos automaticamente para URLs completas (https://).

## 🧠 Benefícios
 
- Automatização de tarefas repetitivas

- Redução de erro humano

- Pronto para rodar em ambientes de testes ou produção