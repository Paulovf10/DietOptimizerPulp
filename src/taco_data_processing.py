from src.taco_data_source import TacoDataSource
import pandas as pd
import numpy as np

class TacoDataProcessing:
    """
    Uma classe para processar e preparar os dados da Tabela TACO.

    Attributes:
        data_source (TacoDataSource): Uma instância da classe TacoDataSource para acessar os dados.
    """

    def __init__(self, data):
        """
        Inicializa a classe com uma instância da TacoDataSource.

        Args:
            filepath (str): O caminho para o arquivo Excel da Tabela TACO.
        """
        self.data_source = data

    def normalize_data(self):
        """
        Normaliza ou padroniza os dados, se necessário.

        Returns:
            dict: Um dicionário com os dados normalizados.
        """
        df_normalized = {
            'id': [int(x) for x in self.data_source['Número'].tolist()],
            'grupo': self.data_source['Grupo'].tolist(),
            'descricao': self.data_source['Descrição do Alimento'].tolist(),
            'kcal': [float(x) if not (isinstance(x, str) or np.isnan(x)) else 0.0 for x in
                     self.data_source['Energia(kcal)'].tolist()],
            'carboidratos': [float(x) if not (isinstance(x, str) or np.isnan(x)) else 0.0 for x in
                             self.data_source['Carboidrato(g)'].tolist()],
            'proteina': [float(x) if not (isinstance(x, str) or np.isnan(x)) else 0.0 for x in
                         self.data_source['Proteína(g)'].tolist()],
            'VitaminaC': [float(x) if not (isinstance(x, str) or np.isnan(x)) else 0.0 for x in
                          self.data_source['VitaminaC(mg)'].tolist()],
            'ferro': [float(x) if not (isinstance(x, str) or np.isnan(x)) else 0.0 for x in
                      self.data_source['Ferro(mg)'].tolist()],
        }
        return df_normalized
