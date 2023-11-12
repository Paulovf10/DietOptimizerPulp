from src.diet_planner import DietPlanner
from src.result_optimizer import ResultOptimizer

def main():
    # Caminho para o arquivo de dados processados da Tabela TACO
    db_path = r'C:\Users\Paulo Victor\PycharmProjects\PO\PO_taco_table_recommender\data\Taco.xlsx'

    # Cria e executa o planejador da dieta
    planner = DietPlanner(db_path)
    planner.run()


    solution = planner.optimizer.solve()

    # Cria e exibe o otimizador de resultado
    result_optimizer = ResultOptimizer(solution, planner.database.get_data(), planner.user_input_handler_collect_food_preferences)
    result_optimizer.display()

if __name__ == "__main__":
    main()
