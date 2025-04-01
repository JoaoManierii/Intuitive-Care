import pandas as pd

class OperadoraModel:
    def __init__(self):
        self.df = pd.read_csv('./Data/operadoras.csv', sep=';', dtype=str)
        self.df.columns = [col.strip().lower().replace(' ', '_') for col in self.df.columns]  # normaliza colunas
        self.df.fillna('', inplace=True)

    def buscar_por_texto(self, texto):
        texto = texto.lower()
        resultados = self.df[self.df.apply(
            lambda row: row.astype(str).str.lower().str.contains(texto).any(), axis=1
        )]
        return resultados.to_dict(orient='records')
