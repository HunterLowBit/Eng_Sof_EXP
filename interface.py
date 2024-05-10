"""
+------------+---------+---------------+---------+---------+
| ITEM       | Wife    | Alternating   | Husband | Jointly |
+------------+---------+---------------+---------+---------+
| Laundry    | 156     | 14            | 2       | 4       |
+------------+---------+---------------+---------+---------+
| Main_meal  | 124     | 20            | 5       | 4       |
+------------+---------+---------------+---------+---------+
| Dinner     | 77      | 11            | 7       | 13      |
+------------+---------+---------------+---------+---------+
| Breakfeast | 82      | 36            | 15      | 7       |
+------------+---------+---------------+---------+---------+
| Tidying    | 53      | 11            | 1       | 57      |
+------------+---------+---------------+---------+---------+
| Dishes     | 32      | 24            | 4       | 53      |
+------------+---------+---------------+---------+---------+
| Shopping   | 33      | 23            | 9       | 55      |
+------------+---------+---------------+---------+---------+
| Official   | 12      | 46            | 23      | 15      |
+------------+---------+---------------+---------+---------+
| Driving    | 10      | 51            | 75      | 3       |
+------------+---------+---------------+---------+---------+
| Finances   | 13      | 13            | 21      | 66      |
+------------+---------+---------------+---------+---------+
| Insurance  | 8       | 1             | 53      | 77      |
+------------+---------+---------------+---------+---------+
| Repairs    | 0       | 3             | 160     | 2       |
+------------+---------+---------------+---------+---------+
| Holidays   | 0       | 1             | 6       | 153     |
+------------+---------+---------------+---------+---------+
"""

import pandas as pd
from scipy.stats import chi2_contingency

from resposta import RespostaChiQuadrado
from dados import Dados
from calculo import CalculoChiQuadrado
from resposta import RespostaChiQuadrado

# Definir o nível de significância alpha
alpha = 0.05

# Criar objeto Dados
dados = Dados()

# Criar DataFrame
dados.criar_dataframe()

# Escolher a característica categórica para análise
caracteristica = "Finances"

dados.escolher_caracteristica(caracteristica)

# Criar objeto CalculoChiQuadrado
calculo = CalculoChiQuadrado(dados.dados_df, caracteristica)

# Calcular o teste qui-quadrado
chi2, p_value, dof, expected = calculo.calcular()

# Criar objeto RespostaChiQuadrado e definir p_value
resposta = RespostaChiQuadrado()
resposta.p_value = p_value

# Imprimir o resultado
resposta.imprimir()

# interface.py
