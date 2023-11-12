import pulp

class DietOptimizer:
    def __init__(self, df_normalized):
        self.data = df_normalized
        self.problem = pulp.LpProblem("Diet_Optimization", pulp.LpMinimize)
        self.food_vars = pulp.LpVariable.dicts("Foods", self.data['id'], lowBound=0)

    def setup_problem(self, nutritional_needs, food_preferences):
        # Restrições nutricionais
        for nutrient, requirement in nutritional_needs.items():
            self.problem += (
                pulp.lpSum([self.food_vars[food_id] * self.data[nutrient][i] for i, food_id in enumerate(self.data['id'])])
                >= float(str(requirement).split(" ")[0]), f"{nutrient}_min"
            )
            self.problem += (
                pulp.lpSum([self.food_vars[food_id] * self.data[nutrient][i] for i, food_id in enumerate(self.data['id'])])
                <= float(str(requirement).split(" ")[1]), f"{nutrient}_max"
            )

        # Restrições de grupo de alimentos por horário
        for time, groups in food_preferences:
            for group in groups:

                food_ids_in_group = [self.data['id'][i] for i, food_group in enumerate(self.data['grupo']) if
                                     food_group == group]
                # Restrição para garantir que pelo menos um alimento de cada grupo seja selecionado no horário especificado
                self.problem += (
                    pulp.lpSum([self.food_vars[food_id] for food_id in food_ids_in_group]) >= 1,
                    f"{time}_{group}_min"
                )

    def solve(self):
        # Soluciona o problema
        self.problem.solve()

        # Verifica o status do problema
        if pulp.LpStatus[self.problem.status] == 'Optimal':
            # Constrói a solução apenas com variáveis que têm um valor definido e são maiores que zero
            solution = {
                food_id: pulp.value(self.food_vars[food_id])
                for food_id in self.data['id']
                if pulp.value(self.food_vars[food_id]) is not None and pulp.value(self.food_vars[food_id]) > 0
            }
            return solution
        else:
            # Se o status não for ótimo, retorna uma mensagem ou o status para depuração
            return {'status': pulp.LpStatus[self.problem.status], 'solution': None}

