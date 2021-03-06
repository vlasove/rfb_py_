# Использование лямбды как параметра функции
# Допустим имеется список из n слов
# Требуется отсортировать этот список в порядке увеличения длины
# каждого слова (в случае, если 2 слова имеют одинаковую длину - их порядок не важен)

words = ["чай" , "кофе", "кисель", "сок", "компот", "вода", "новогодний пунш"]
# ["сок" , "чай", "кофе", "вода", "компот", "кисель", "новогодний пунш"]

# 1. На основе нашего списка пусть питон создаст список, состоящий из длин строк
                       # ["чай" , "кофе", "кисель", "сок", "компот", "вода", "новогодний пунш"]
#words -> PYTHON MAGIC -> [3,        4,      6,        3,       6,      4,          15]

# 2. Хотелось бы сортировать второй список и видеть изменения в первом
# ["чай" , "сок", "вода", "кофе", "компот", "кисель", "новогодний пунш"]
[3,        3,     4,        4,       6,      6,          15]

# 3. Вернуть исходный список слов
["чай" , "сок", "вода", "кофе", "компот", "кисель", "новогодний пунш"]


print("Words origin:", words)
words.sort(key=lambda word : len(word))

print("Words sorted by len:", words)