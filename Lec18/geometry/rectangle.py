"""
Модуль содержит функции для
расчета периметра и площади прямоугольника
"""
print("rectangle.py works")

def perimeter(width:float, length:float) -> float:
    """
    Периметр 2 * (width + length)
    """
    return 2 * (width + length)

def area(width:float, length:float) -> float:
    """
    Площадь width * length
    """
    return width * length