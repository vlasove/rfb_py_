# while expression:
#     body

# Простейшие пример работы с циклом while
i = 0                       # Переменная цикла
while i <= 10:              # Условие цикла
    print("Current i:", i)  # Тело цикла
    i = i + 1               # Измнение переменной цикла


# Условно-бесконечный while и первое ключевое слово break
while True:
    numeric = int(input())
    if numeric >= 100 and numeric % 2 ==0:
        print("It's over")
        break
    if numeric % 9 == 0:
        print("Numeric % 9 and continue")
        continue
    print("Current numeric:", numeric)

print("Out of while body")