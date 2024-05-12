from scipy.stats import chi2_contingency
import numpy as np


data = np.array([[156, 124, 77, 82, 53, 32, 33, 12, 10, 13, 8, 0, 0],
    [14, 20, 11, 36, 11, 24, 23, 46, 51, 13, 1, 3, 1],
    [2, 5, 7, 15, 1, 4, 9, 23, 75, 21, 53, 160, 6],
    [4, 4, 13, 7, 57, 53, 55, 15, 3, 66, 77, 2, 153]])

chi2, p, dof, expected = chi2_contingency(data)

with open("Resposta.txt", "w") as f:
    f.write(f"Chi-squared statistic: {chi2:.13f}\n")
    f.write(f"P-value: {p:.2f}\n")
    f.write(f"Degrees of freedom: {dof:.2f}\n")
    f.write(f"Expected frequencies: \n")
    np.savetxt(f, expected, fmt='%1.8f')

print(f"Chi-squared statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print(f"Expected frequencies: \n, {expected}")
