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