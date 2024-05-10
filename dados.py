import pandas as pd


class Dados:
    def __init__(self):
        self.dados = {
            "ITEM": [
                "Laundry",
                "Main_meal",
                "Dinner",
                "Breakfeast",
                "Tidying",
                "Dishes",
                "Shopping",
                "Official",
                "Driving",
                "Finances",
                "Insurance",
                "Repairs",
                "Holidays",
            ],
            "Wife": [156, 124, 77, 82, 53, 32, 33, 12, 10, 13, 8, 0, 0],
            "Alternating": [14, 20, 11, 36, 11, 24, 23, 46, 51, 13, 1, 3, 1],
            "Husband": [2, 5, 7, 15, 1, 4, 9, 23, 75, 21, 53, 160, 6],
            "Jointly": [4, 4, 13, 7, 57, 53, 55, 15, 3, 66, 77, 2, 153],
        }
        self.criar_dataframe()

    def criar_dataframe(self):
        self.dados_df = pd.DataFrame(self.dados)
        self.dados_df.set_index("ITEM", inplace=True)

    def escolher_caracteristica(self, caracteristica):
        self.caracteristica = caracteristica


# r:/GITHUB/Eng_Sof_EXP/dados.py
