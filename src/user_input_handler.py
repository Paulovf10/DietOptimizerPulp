class UserInputHandler:
    """
    Classe para lidar com os inputs dos usuários no Sistema de Recomendação de Dieta.

    Esta classe irá interagir com o usuário para coletar informações sobre suas necessidades
    nutricionais, restrições e preferências dietéticas, bem como o orçamento disponível para a dieta.
    """

    def __init__(self):
        """
        Inicializa a classe com os atributos necessários para armazenar os inputs do usuário.
        """
        self.nutritional_needs = {}
        self.dietary_restrictions = []
        self.food_preferences = []
        self.budget = None

    def collect_nutritional_needs(self):
        """
        Solicita ao usuário para inserir suas necessidades nutricionais diárias.
        """
        print("Por favor, insira suas necessidades nutricionais diárias.")
        # self.nutritional_needs['kcal'] = (input("Calorias (kcal): "))
        # self.nutritional_needs['proteina'] = (input("Proteínas (g): "))
        # self.nutritional_needs['carboidratos'] = (input("Carboidratos (g): "))
        # self.nutritional_needs['VitaminaC'] = (input("VitaminaC(mg): "))
        # self.nutritional_needs['ferro'] = (input("Ferro (mg): "))

        self.nutritional_needs['kcal'] = "1 3000"
        self.nutritional_needs['proteina'] = "1 50"
        self.nutritional_needs['carboidratos'] = "1 200"
        self.nutritional_needs['VitaminaC'] = "1 10"
        self.nutritional_needs['ferro'] = "1 20"
        return self.nutritional_needs

    def collect_food_preferences(self):
        """
        Solicita ao usuário para listar alimentos preferidos que gostaria de incluir na dieta para cada horário específico.
        """
        # grupo_nomes = {
        #     '1': "Cereais e derivados",
        #     '2': "Verduras, hortaliças e derivados",
        #     '3': "Frutas e derivados",
        #     '4': "Gorduras e óleos",
        #     '5': "Pescados e frutos do mar",
        #     '6': "Carnes e derivados",
        #     '7': "Leite e derivados",
        #     '8': "Bebidas (alcoólicas e não alcoólicas)",
        #     '9': "Ovos e derivados",
        #     '10': "Produtos açucarados",
        #     '11': "Miscelâneas",
        #     '12': "Outros alimentos industrializados",
        #     '13': "Alimentos preparados",
        #     '14': "Leguminosas e derivados",
        # }
        #
        # print("Monte seu grupo de alimentação da dieta.")
        # print("Digite 'done' para terminar ou 'next' para seguir para o próximo horário.")
        # self.food_preferences = []  # Garante que a lista esteja vazia antes de começar
        # while True:
        #     horario = input("Horário: ")
        #     if horario.lower() == 'done':
        #         break
        #
        #     grupos_horario = []
        #     print("Selecione os grupos de alimentos para o horário: " + horario)
        #     while True:
        #         grupo_digitado = input(
        #             "1 - Cereais e derivados\n2 - Verduras, hortaliças e derivados\n3 - Frutas e derivados\n4 -Gorduras e óleos\n5 - "
        #             "Pescados e frutos do mar\n6 - Carnes e derivados\n7 - Leite e derivados\n8 - Bebidas (alcoólicas e não alcoólicas)"
        #             "\n9 - Ovos e derivados\n10 - Produtos açucarados\n11 - Miscelâneas\n12 - Outros alimentos industrializados\n13 - "
        #             "Alimentos preparados\n14 - Leguminosas e derivados\n\nDigite o número do grupo de alimentos ou 'next' para seguir: ")
        #
        #         if grupo_digitado.lower() == 'next':
        #             break
        #         elif grupo_digitado.lower() == 'done':
        #             return self.food_preferences
        #
        #         grupo_nome = grupo_nomes.get(grupo_digitado)
        #         if grupo_nome:
        #             grupos_horario.append(grupo_nome)
        #         else:
        #             print("Número de grupo inválido, tente novamente.")
        #
        #     if grupos_horario:
        #         self.food_preferences.append((horario, grupos_horario))

        self.food_preferences = [
            ("8:00", ["Leite e derivados", "Ovos e derivados"]),
            ("12:00", ["Cereais e derivados", "Gorduras e óleos", "Ovos e derivados", "Verduras, hortaliças e derivados", "Carnes e derivados"]),
            ("15:00", ["Frutas e derivados", "Leite e derivados"]),
            ("20:00", ["Outros alimentos industrializados", "Bebidas (alcoólicas e não alcoólicas)"]),
        ]

        return self.food_preferences

