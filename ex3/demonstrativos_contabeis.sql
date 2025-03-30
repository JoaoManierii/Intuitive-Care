-- Criação inicial da tabela
CREATE TABLE demonstrativos_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    registro_ans VARCHAR(10),
    codigo_contabil VARCHAR(20),
    descricao TEXT,
    valor_saldo_inicial NUMERIC,
    valor_saldo_final NUMERIC,
    FOREIGN KEY (registro_ans) REFERENCES operadoras_ativas(registro_ans)
);

-- Remoção das colunas vazias da importação inicial
ALTER TABLE demonstrativos_contabeis
DROP COLUMN registro_ans,
DROP COLUMN codigo_contabil,
DROP COLUMN valor_saldo_inicial,
DROP COLUMN valor_saldo_final;

-- Renomeando as colunas corretas com dados válidos
ALTER TABLE demonstrativos_contabeis
RENAME COLUMN reg_ans TO registro_ans;

ALTER TABLE demonstrativos_contabeis
RENAME COLUMN cd_conta_contabil TO codigo_contabil;

ALTER TABLE demonstrativos_contabeis
RENAME COLUMN vl_saldo_inicial TO valor_saldo_inicial;

ALTER TABLE demonstrativos_contabeis
RENAME COLUMN vl_saldo_final TO valor_saldo_final;

-- Ajustando o tipo de dado da chave estrangeira para compatibilidade
ALTER TABLE demonstrativos_contabeis
ALTER COLUMN registro_ans TYPE VARCHAR USING registro_ans::VARCHAR;
