"""
Общий синтаксис
lst = [elem for elem in iter]
"""

# Список из 100 нулей
zeros = [0 for _ in range(100)]
#print(zeros)

# Список из первых 100 натуральных чисел
numerics = [i for i in range(100)]
# print(numerics)

# Списочное выражение работает быстрее
# чем его аналог в виде цикла for с добавлением элементов

# a = val1 if expression else val2
nums = [i ** 2 if i % 2 ==0 else i ** 3 for i in range(100)]
print(nums)















