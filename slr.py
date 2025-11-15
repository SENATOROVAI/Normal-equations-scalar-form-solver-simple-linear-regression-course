import pandas as pd

points = list(pd.read_csv('https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/single_independent_variable_linear_small.csv', delimiter=",").itertuples())
n = len(points)
m = (n*sum(p.x*p.y for p in points) - sum(p.x for p in points) * sum(p.y for p in points)) / (n*sum(p.x**2 for p in points) - sum(p.x for p in points)**2)
b = (sum(p.y for p in points) / n) - m * sum(p.x for p in points) / n
print(m, b)
