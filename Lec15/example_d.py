"""
Пример аннотаций
"""
from typing import List, Dict

def mutate(a:int, b:int, d : List[int]) -> List[int]:
    """
    Никто не знает как работает эта функция.
    Служит для примера аннотиций входных и выходных типов
    """
    return [a,b] + d

def build_map(key:str = "key", value:int=10) -> Dict[str, int] :
    """
    Строит словарь , где ключ - аргумент key
    а значение - аргумент value
    """
    return {key : value}

build_map()