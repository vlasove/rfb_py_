# Гадость 2 - синонимичное приведение логического выражения
if not None and 10 or "asd" and not False:
    print("Foo")
else:
    print("Buzz")

# Synonimic type casting in logical expression
# Если в логичeском выражении результат - число, то:
#       если число != 0 -> True
#       если число == 0 -> False

# Если в логическом выражении результат - строка, то:
#      если строка != "" -> True
#      если строка == "" -> False

# None -> False
# not Nont -> True


"""
Как хранятся переменные в runtime?
Когда определяем переменную в какой-либо области видимости - для этой области ДОЛЖЕН создаваться
отдельный СТЕК для хранения этих переменных (нужен для сборщика мусора)
"""