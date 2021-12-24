# Пример функции со значениями по умолчанию
def add(a = 3, b = 4):
    return a + b


print("10 + 20 = ", add(10, 20))
print("10 + ? = ", add(10))
print("? + ? = ", add())