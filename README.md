
# 🧪 - Intuitive Care

Este repositório contém a resolução dos quatro exercícios propostos. Cada exercício aborda uma habilidade prática diferente.

---

## 📁 Estrutura

```
.
├── ex1/    # Web Scraping e Download de PDFs
├── ex2/    # Extração e Tratamento de Dados de PDF
├── ex3/    # Banco de Dados com PostgreSQL (DBeaver)
├── ex4/    # API com Flask + Frontend em Vue.js
```

---

## ✅ Exercícios

### 1. Download e Compactação de Anexos (.zip)
- Acessa site da ANS e baixa os Anexos I e II em PDF
- Salva os arquivos em pasta local e compacta em ZIP
- Realizado com `requests`, `bs4`, `zipfile` e boas práticas

### 2. Extração de Dados do PDF e Transformação em CSV
- Extrai dados tabulares do PDF do Anexo I usando `pdfplumber`
- Salva em `.csv` e compacta
- Substitui abreviações pelas descrições completas

### 3. Criação e Consulta em Banco de Dados
- Criação de tabelas e importação dos dados (CSV e Demonstrativos ANS)
- Consultas SQL analíticas com PostgreSQL (via DBeaver)
- Consultas respondem às despesas das operadoras por trimestre e ano

### 4. API e Frontend Integrado
- Backend em Flask com leitura de dados de operadoras
- Rota `/buscar` com busca textual
- Frontend em Vue.js com Tailwind CSS para exibir resultados de forma responsiva

---

## 👨‍💻 Autor

João Otávio Manieri  
