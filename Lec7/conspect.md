## Лекция 7. Коллекции. Строки

**Строка** (str) - это упорядоченная (индексируемая) коллекция, способная хранить элементы ОДНОГО типа.

### 1. Индексация в строках.
```
# Строки. Индексация

message = "Hello World!"
print("First letter:", message[0])
print("First letter type:", type(message[0]))

print("Second letter:", message[1])


print("Last letter:", message[len(message) - 1])
print("Pre-last letter:", message[len(message) - 2])

# Синтаксический сахар "отрицательных индексов" (не нужно писать len(message))
print("Last letter:", message[-1])
print("Pre-last letter:", message[-2])

# Итерирование по индексам
for i in range(len(message)): #range(start=0, stop[, step=1)
    print(f"Letter {i} is {message[i]}")
```

### 2. Сравнение строк
```
# Сравнение строк
lhs_word = "abcd"
rhs_word = "abc"

print(lhs_word < rhs_word)
# ord(str) -> int, chr(int) -> str
# В Python все строки хранятся как unicode
# ASCII - сколько всего символов в стандарте
print("Code a is :", ord("a"))
print("Code is A:", ord("A"))
print("Code B is:", ord("B"))
print("Code Y is:", ord("Y"))

# for i in range(60, 150):
#     print(f"Character of {i}:", chr(i))

# Как сравниваются строки?
# "abcd"   <    "abc"
# 1)  ord("a")  ==   ord("a")
# 2)  ord("b")  ==   ord("b") 
# 3)  ord("c")  ==   ord("c")
# 4)  ord("d")  >>   А ТУТ НЕТ БУКВЫ :) -> False
```

### 3. Срезы (слайсы) строк
```
```

