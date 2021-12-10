## Лекция 3. Базовые типы в Python

В `Python` есть 5 базовых типов:
* `int` - целые числа
* `float` - вещественные числа
* `bool` - булев тип
* `str` - строки
* `NoneType` - тип "без значения"

### 1. Целые числа
```
# Целые числа
a_int = 4
b_int = 3

print(f"A value {a_int} and B value {b_int}")
print("Type of A:", type(a_int))
print(a_int, b_int)

# Арифметика
print("a_int + b_int = ", a_int + b_int)
print("a_int - b_int = ", a_int - b_int)
print("a_int * b_int = ", a_int * b_int)
# Нюанс при делении - всегда вещественное число!!!
print("a_int / b_int = ", a_int / b_int)
# Классическое целочисленное деление - это //
print("a_int // b_int = ", a_int // b_int)
# Взятие остатка от деления
print("a_int % b_int = ", a_int % b_int)
# Возведение в степень
print("a_int ^ b_int = ", a_int ** b_int)
```

* Считывание целых чисел:
```
a_int = int(input())
b_int = int(input())

print(a_int * b_int)
```
* Выше представлен пример **явного приведения типов в Python** (приводим строку к целому числу).
* Чтобы строковый литерал преобразовать к целому числу:
    * 1) Литерал состоит ТОЛЬКО из символов цифр
    * 2) Допускается наличие одного знака `-` в самом начале!


### 2. Вещественные числа
```
# Вещественные числа
a_float = 2.5 #float(input())
b_float = 3.7 #float(input())



print(f"A value {a_float} and B value {b_float}")
print("Type of A:", type(a_float))
print(a_float, b_float)

# Арифметика
print("a_float + b_float = ", a_float + b_float)
print("a_float - b_float = ", a_float - b_float)
print("a_float * b_float = ", a_float * b_float)
# # Нюанс при делении - всегда вещественное число!!!
print("a_float / b_float = ", a_float / b_float)
# Классическое целочисленное деление - это //
print("a_float // b_float = ", a_float // b_float)
# Взятие остатка от деления
print("a_float % b_float = ", a_float % b_float)
# Возведение в степень
print("a_float ^ b_float = ", a_float ** b_float)
```

* Считывание вещественных чисел:
```
a_float = float(input())
b_float = float(input())

print(a_float * b_float)
```
* Выше представлен пример **явного приведения типов в Python** (приводим строку к целому числу).
* Чтобы строковый литерал преобразовать к вещественному числу числу:
    * 1) Литерал состоит ТОЛЬКО из символов цифр
    * 2) Допускается минус в начале
    * 3) Допускается наличие одной точки

#### Неявное преобразование типов
* 1) Выполнение арифметики между int\float
```
# Неявное преобразование типов
a_int = 10
b_float = 12.5

res = a_int + b_float ** 2 # float(a_int) + b_float ** float(2)
print(res)
```

* При выполенении арифметических операций между набором чисел, как целых, так и вещественных, интерпретатор НЕЯВНО приведет все целые числа к вещественным .