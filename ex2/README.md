# 📊 Teste de Transformação de Dados – ANS (Anexo I)

Este projeto automatiza a extração, transformação e compactação dos dados da tabela **Rol de Procedimentos e Eventos em Saúde** a partir do **Anexo I em PDF** disponibilizado pela ANS. O objetivo é estruturar esses dados em formato `.csv` para análise, seguindo os critérios do teste proposto.

---

## ⚙️ Funcionalidades implementadas

- 🔍 Abertura e leitura de todas as páginas do PDF `Anexo_I.pdf`.
- 📥 Extração de todas as tabelas contidas no documento.
- 📄 Conversão das tabelas em um único arquivo `.csv`, estruturado.
- 🔁 Substituição de abreviações:
  - `OD` → `Odontologia`
  - `AMB` → `Ambulatorial`
  - `HCO` → `Seg. Hospitalar Com Obstetrícia`
  - `HSO` → `Seg. Hospitalar Sem Obstetrícia`
  - `REF` → `Plano Referência`

- 🗜️ Geração de um arquivo `.zip` com o nome `Teste_JoaoOtavio.zip`, contendo o `.csv`.

---

## 🧪 Como executar

### 1. Instalar as dependências

```bash
pip install pdfplumber pandas
```

2. Estrutura de pastas esperada

```python
├── ex2/
│   ├── anexos/
│   │   └── Anexo_I.pdf
│   ├── ex2.py
│   └── (gerados após execução)
│       ├── Rol_de_Procedimentos.csv
│       └── Teste_JoaoOtavio.zip
```

3. Executar o script

```python 
python ex2.py
```

## 📁 Saída gerada

- Rol_de_Procedimentos.csv: arquivo estruturado com os dados extraídos.
- Teste_JoaoOtavio.zip: arquivo compactado contendo o .csv.

## 📌 Tecnologias utilizadas

- Python 3
- pdfplumber – extração de dados de PDF
- pandas – manipulação de tabelas e substituições
- zipfile – compactação final

## 💡 Melhorias possíveis
- ✅ Reconhecimento automático da legenda do rodapé do PDF, substituindo abreviações de forma dinâmica em vez de fixa.

- 📐 Padronização e limpeza de colunas, como remover quebras de linha em headers (RN\n(alteração) → RN (alteração)).
- 🧠 Identificação e remoção de colunas vazias ou repetidas, garantindo um CSV mais enxuto.
- 🔎 Validação de dados (e.g., verificar se todas as linhas têm o mesmo número de colunas).
