# Супер-простой цикл (вводим и сразу выводим числа ДО ТЕХ пор пока не введен 0)
# Решение G
while True:
    numeric = int(input())
    if numeric == 0:
        break
    print(numeric)