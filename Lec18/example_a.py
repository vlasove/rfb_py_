"""
Модуль содержащий набор элементов
для последующего взаимодействия с ними
через импортирование
"""

def add(x_arg:int, y_arg:int) -> int:
    """
    Сложение вида x^3 + y ^4
    """
    return x_arg ** 3 + y_arg ** 4


MAX_ATTEMPTS = 11
date = "2021-27-12"

def main() -> None:
    """
    """
    for i in range(MAX_ATTEMPTS):
        print("Res:", add(i, i + MAX_ATTEMPTS))
        if i > 3 :
            break

if __name__ == '__main__':
    main()