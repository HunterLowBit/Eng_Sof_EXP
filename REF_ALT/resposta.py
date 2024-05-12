class RespostaChiQuadrado(object):

    def __init__(self):
        self._p_value = None
        self._alpha = None

    @property
    def p_value(self):
        return self._p_value

    @p_value.setter
    def p_value(self, value):
        self._p_value = value

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    def imprimir(self):
        if self.p_value is not None and self.alpha is not None:
            if self.p_value < self.alpha:
                print(
                    "Rejeitamos a hipótese nula (H0). As frequências das categorias são diferentes das esperadas."
                )
            else:
                print(
                    "Não rejeitamos a hipótese nula (H0). Não há evidências suficientes para afirmar que as frequências das categorias são diferentes das esperadas."
                )
        else:
            print("Erro: Resultados não definidos.")


# r:/GITHUB/Eng_Sof_EXP/resposta.py
