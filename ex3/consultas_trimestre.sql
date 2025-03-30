-- Consulta: Top 10 operadoras com maiores despesas
-- no 4º trimestre de 2024, na categoria:
-- "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"

SELECT 
    o.razao_social,
    d.registro_ans,
    SUM(REPLACE(d.valor_saldo_final, ',', '.')::NUMERIC) AS total_despesas
FROM demonstrativos_contabeis d
JOIN operadoras_ativas o ON o.registro_ans = d.registro_ans
WHERE
    d.descricao ILIKE '%SINISTROS CONHECIDOS OU AVISADOS%' AND
    d.descricao ILIKE '%ASSISTÊNCIA A SAÚDE%' AND
    d.descricao ILIKE '%HOSPITALAR%' AND
    d.data >= DATE '2024-10-01' AND
    d.data <= DATE '2024-12-31' AND
    d.valor_saldo_final IS NOT NULL
GROUP BY o.razao_social, d.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;
