# Неявное преобразование типов
a_int = 10
b_float = 12.5

res = a_int + b_float ** 2 # float(a_int) + b_float ** float(2)
print(res)