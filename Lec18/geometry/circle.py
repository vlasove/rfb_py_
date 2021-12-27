"""
Модуль содержит функции для
расчета периметра и площади круга
"""
import math as m

print("circle.py works")

def perimeter(radius:float) -> float:
    """
    Длина окружности 2 * pi * radius
    """
    return 2 * m.pi * radius

def area(radius:float) -> float:
    """
    Площадь pi * r ^ 2
    """
    return m.pi * radius ** 2