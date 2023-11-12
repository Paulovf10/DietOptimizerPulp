from src.user_input_handler import UserInputHandler
from src.taco_database import TacoDatabase
from src.diet_optimizer import DietOptimizer


class DietPlanner:
    """
    Classe para coordenar a entrada de parâmetros do usuário, consultar a base de dados e
    executar a otimização da dieta.

    Esta classe funciona como a camada intermediária entre o usuário e o sistema de otimização,
    garantindo que todas as informações necessárias sejam coletadas e processadas adequadamente.
    """

    def __init__(self, db_path):
        """
        Inicializa a classe com o caminho para a base de dados.

        Args:
            db_path (str): O caminho para o arquivo de dados processados.
        """
        self.user_input_handler_collect_food_preferences = None
        self.user_input_handler_nutritional_needs = None
        self.db_path = db_path
        self.user_input_handler = UserInputHandler()
        self.database = TacoDatabase(db_path)
        self.database.get_data()
        self.optimizer = None

    def run(self):
        """
        Executa o processo completo de planejamento da dieta, desde a coleta de inputs até a otimização.
        """
        # Coleta de inputs do usuário
        self.user_input_handler_nutritional_needs = self.user_input_handler.collect_nutritional_needs()
        self.user_input_handler_collect_food_preferences = self.user_input_handler.collect_food_preferences()
        # Carregamento de dados da base de dados
        data = self.database.get_data()

        # Configuração e execução do otimizador
        self.optimizer = DietOptimizer(data)
        self.optimizer.setup_problem(self.user_input_handler_nutritional_needs,
                                     self.user_input_handler_collect_food_preferences)
        solution = self.optimizer.solve()


