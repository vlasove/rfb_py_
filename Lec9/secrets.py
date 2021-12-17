# Секретная вещь №1
a = b = c = d = 1 # Сквозное присваивание переменных

# Секретная вещь №2
lhs, _, rhs = [10, 20, 30] # Распаковка списка
print(lhs, rhs)

# Секретная вещь №3
# Тернарный условный оператор
age = 19
supported_client = "Android X2. Kitkat" if age > 18 else "Android KETKAT 9000"
print(supported_client)

# Секретная вещь №4
# Итерирование парой элементов

lst = [
    [10, 20],
    [30, 40],
    [50, 60],
]

for i, j in lst: # i,j = [30, 40]
    print(i, j)