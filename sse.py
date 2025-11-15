m = 1.93939394
b = 4.73333333
sum_of_squares = 0.0
# Вычисляем сумму квадратов
for p in points:
    y_actual = p.y
    y_predict = m*p.x + b
    residual_squared = (y_predict - y_actual)**2
    sum_of_squares += residual_squared
print(f"Сумма квадратов = {sum_of_squares}")
