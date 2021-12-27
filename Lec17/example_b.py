# Создадим список - мутант, который будет состоять из элементов,
# Расчитывающихся по формуле i**2 + i ** 3 - i ** 0.5,
# где i - индекс элемента в списке

calculate_elem  = lambda i: i ** 2 + i ** 3 - i ** 0.5
numerics = [calculate_elem(i) for i in range(1, 100)]

print(numerics)