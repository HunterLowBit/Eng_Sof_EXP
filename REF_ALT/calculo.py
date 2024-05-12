from scipy.stats import chi2_contingency


class CalculoChiQuadrado:
    def __init__(self, dados_df, caracteristica):
        self.dados_df = dados_df
        self.caracteristica = caracteristica

    def calcular(self):
        frequencias_obs = self.dados_df.loc[self.caracteristica]

        # Verificar se há algum valor zero
        if (frequencias_obs == 0).any():
            print("Erro: A sequência contém um valor zero.")
            return None, None, None, None

        chi2, p_value, dof, expected = chi2_contingency(frequencias_obs)
        return chi2, p_value, dof, expected


# r:/GITHUB/Eng_Sof_EXP/calculo.py
