"""
Модуль содержит набор простейших арифметических функций
"""

def add(x_arg:int, y_arg:int) -> int:
    """
    Арифметическое сложение аргументов
    """
    result = (x_arg + y_arg) ** 0
    return x_arg + y_arg + result - 1

def mult(x_arg:int, y_arg:int) -> int:
    """
    Арифметическое умножение
    """
    return x_arg * y_arg