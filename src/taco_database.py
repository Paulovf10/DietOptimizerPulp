import pandas as pd


class TacoDatabase:
    """
    Classe para acessar a base de dados da Tabela TACO após o processamento.

    Esta classe serve como uma camada de abstração somente para leitura dos dados processados,
    facilitando o acesso aos dados pela aplicação de otimização.

    Attributes:
        db_path (str): O caminho para o arquivo de banco de dados ou arquivo de dados processados.
    """

    def __init__(self, db_path):
        """
        Inicializa a classe TacoDatabase.

        Args:
            db_path (str): O caminho para o arquivo de banco de dados ou arquivo de dados processados.
        """
        self.db_path = db_path
        self.dataframe = self.load_data()

    def load_data(self):
        """
        Carrega os dados processados para a memória a partir do arquivo de dados.

        Returns:
            pd.DataFrame: O DataFrame carregado com os dados processados.
        """
        try:
            df = pd.read_excel(self.db_path)
            return df
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {self.db_path}")
            return pd.DataFrame()  # Retorna um DataFrame vazio se o arquivo não for encontrado
        except Exception as e:
            print(f"Ocorreu um erro ao carregar o arquivo: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio se ocorrer algum outro erro

    def get_data(self):
        """
        Obtém os dados carregados.

        Returns:
            pd.DataFrame: O DataFrame carregado com os dados processados.
        """
        return self.dataframe



"""# Caminho para o arquivo de dados processados
db_path = '../data/Taco.xlsx'

# Criação da instância de TacoDatabase
taco_db = TacoDatabase(db_path)

# Acessando dados processados
dados_processados = taco_db.get_data()
print(dados_processados.head())  # Exibe as primeiras linhas dos dados processados
"""