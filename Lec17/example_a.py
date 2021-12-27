"""
Анонимные функции
"""
# Куча кода
def add(x_arg:int, y_arg:int) ->int:
    """
    x^3 + y^2
    """
    return x_arg ** 3 + y_arg ** 2

anon_add = lambda : x**3 + y**2

res = anon_add(2,3) + anon_add(3,2) 
print(res)

# Куча кода