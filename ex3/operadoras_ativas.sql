-- Criação inicial da tabela
CREATE TABLE operadoras_ativas (
    registro_ans VARCHAR(10) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_comercializacao TEXT,
    data_registro_ans DATE
);

-- Remoção das colunas importadas vazias
ALTER TABLE operadoras_ativas
DROP COLUMN email,
DROP COLUMN regiao_comercializacao;

-- Renomeando as colunas com dados reais
ALTER TABLE operadoras_ativas
RENAME COLUMN endereco_eletronico TO email;

ALTER TABLE operadoras_ativas
RENAME COLUMN regiao_de_comercializacao TO regiao_comercializacao;
