# Функция с аргументами (простейшие)
def add(a, b):
    res = a**2 + b**2 - 3*a*b
    return res

default_result = add(10, 50)
print(default_result)