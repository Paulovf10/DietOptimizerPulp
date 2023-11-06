from taco_data_source import TacoDataSource
import pandas as pd


class TacoDataProcessing:
    """
    Uma classe para processar e preparar os dados da Tabela TACO.

    Attributes:
        data_source (TacoDataSource): Uma instância da classe TacoDataSource para acessar os dados.
    """

    def __init__(self, filepath):
        """
        Inicializa a classe com uma instância da TacoDataSource.

        Args:
            filepath (str): O caminho para o arquivo Excel da Tabela TACO.
        """
        self.data_source = TacoDataSource(filepath)

    def clean_data(self):
        """
        Realiza a limpeza dos dados, como tratar valores ausentes e remover duplicatas.

        Returns:
            pd.DataFrame: Um DataFrame com os dados limpos.
        """
        df = self.data_source.dataframe
        # Exemplo: remover linhas com valores ausentes
        df_clean = df.dropna()
        # Exemplo: remover duplicatas
        df_clean = df_clean.drop_duplicates()
        self.data_source.dataframe = df_clean
        return df_clean

    def normalize_data(self):
        """
        Normaliza ou padroniza os dados, se necessário.

        Returns:
            pd.DataFrame: Um DataFrame com os dados normalizados.
        """
        # Implemente a normalização/padronização conforme necessário
        # Este é apenas um placeholder para ilustrar onde você faria isso.
        df_normalized = self.data_source.dataframe
        return df_normalized




