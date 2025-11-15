import pandas as pd

points = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/single_independent_variable_linear_small.csv", delimiter=",").itertuples()

m = 1.93939394
b = 4.73333333
# Вычисляем остатки
for p in points:
    y_actual = p.y
    y_predict = m*p.x + b
    residual = y_actual - y_predict
    print(residual)
  
