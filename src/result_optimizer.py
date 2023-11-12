class ResultOptimizer:
    """
    Classe para interpretar e apresentar os resultados da otimização da dieta em linguagem natural.
    """

    def __init__(self, solution, data, food_preferences):
        """
        Inicializa a classe com a solução da otimização da dieta.

        Args:
            solution (dict): A solução da otimização da dieta.
            data (dict): Dados normalizados com informações sobre os alimentos.
            food_preferences (list): Lista de preferências alimentares com horários.
        """
        self.solution = solution
        self.data = data
        self.food_preferences = food_preferences

    def generate_summary(self):
        """
        Gera um resumo dos resultados em linguagem natural.

        Returns:
            str: Um resumo descritivo da solução otimizada da dieta.
        """
        summary = "Resumo da Dieta Otimizada:\n"
        if not self.solution:
            return "Não foi possível encontrar uma solução ótima com os dados e restrições fornecidos."

        # Mapeia os IDs dos alimentos para seus nomes e grupos
        food_mapping = {food_id: food_name for food_id, food_name in zip(self.data['id'], self.data['descricao'])}

        # Organiza os alimentos por horário
        for time, groups in self.food_preferences:
            summary += f"Para o horário das {time}, consuma:\n"
            # Filtra os alimentos da solução que pertencem aos grupos desejados
            for group in groups:
                foods_in_group = [food_id for food_id, grupo in zip(self.data['id'], self.data['grupo']) if
                                  grupo == group]
                for food_id in foods_in_group:
                    if food_id in self.solution and self.solution[food_id] > 0:
                        summary += f" - {food_mapping[food_id]}: {self.solution[food_id]} gramas\n"
            summary += "\n"

        return summary

    def display(self):
        """
        Exibe o resumo da solução otimizada da dieta e grava em um arquivo .txt.
        """
        summary = self.generate_summary()
        print(summary)  # Exibe o resumo no console

        # Grava o resumo em um arquivo .txt
        with open(r'C:\Users\Paulo Victor\PycharmProjects\PO\PO_taco_table_recommender\results/summary.txt', 'w') as file:
            file.write("Introdução ao Resumo da Dieta Otimizada\n")
            file.write(
                "Este documento apresenta um resumo da dieta otimizada com base em suas preferências e necessidades nutricionais.\n\n")
            file.write(summary)