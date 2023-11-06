import pandas as pd


class TacoDataSource:
    """
    Uma classe para acessar e manipular dados da Tabela TACO.

    Attributes:
        filepath (str): O caminho para o arquivo Excel da Tabela TACO.
        dataframe (pd.DataFrame): O DataFrame que armazena os dados carregados do Excel.
    """

    def __init__(self, filepath):
        """
        Inicializa a classe com o caminho do arquivo e carrega os dados para um DataFrame.

        Args:
            filepath (str): O caminho para o arquivo Excel da Tabela TACO.
        """
        self.filepath = filepath
        self.dataframe = self.load_taco_data()

    def load_taco_data(self):
        """
        Carrega os dados da Tabela TACO do arquivo Excel especificado.

        Returns:
            pd.DataFrame: Um DataFrame contendo os dados carregados ou None se o arquivo não for encontrado.
        """
        try:
            df = pd.read_excel(self.filepath)
            return df
        except FileNotFoundError:
            print(f"O arquivo {self.filepath} não foi encontrado.")
            return None

    def inspect_data(self):
        """
        Imprime informações básicas sobre o DataFrame, incluindo a contagem de valores não nulos e a soma de valores nulos.
        """
        if self.dataframe is not None:
            print(self.dataframe.info())
            print(self.dataframe.isnull().sum())

    def get_summary_statistics(self):
        """
        Apresenta estatísticas descritivas para colunas numéricas do DataFrame.

        Returns:
            pd.DataFrame: Um DataFrame contendo estatísticas descritivas, como média, mediana, máximo, mínimo e desvio padrão.
        """
        if self.dataframe is not None:
            return self.dataframe.describe()

    def save_cleaned_data(self, new_filepath):
        """
        Salva o DataFrame limpo para um novo arquivo Excel.

        Args:
            new_filepath (str): O caminho do arquivo onde o DataFrame limpo será salvo.
        """
        if self.dataframe is not None:
            self.dataframe.to_excel(new_filepath, index=False)


