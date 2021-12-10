## Лекция 4. Условный оператор

* Условный оператор - это управляющая конструкция, позволяющая выполнять блок кода в случа истинности какого-либо логического выражения.

### 1. Какие логически выражения бывают?
* Логическое выражение (expression) - конструкция, принимающая значения True или False.
* 1) Осн. на числовых типах
```
a_int = 100
b_int = 200.5

# Сравнение 
print(" > ", a_int > b_int)
print(" < ", a_int < b_int)
print(" >= ", a_int >= b_int)
print(" <= ", a_int <= b_int)

print(" == ", a_int == b_int)
print(" != ", a_int != b_int)

# Четное ли число 100?
print(100 % 2 == 0)

# Комбинирование
print(" > and !=", (a_int > b_int) and (b_int != 15))
```

* 2) Осн. на строковом типе
```
message = "Hello world!"

# Сводя условие к длине строке - справедливы все операции как над числами
print(len(message) >= 7)

# Проверка вхождения ПОДСТРОКИ в СТРОКУ
print("wor" in message)

# Прямое сравнение строк
print("hello" == "hello")
print("+" != "-")
```

### 2. Синтаксис одиночного условного оператора:
```
if expression:
    body
```
Пример:
```
age = int(input())

if age >= 18:
    print("Your age is:", age)
    print("Welcome to our service!")
    print("Press here to continue!")

print("Service done!")
```

### 3. Условный оператор с блоком else
```
if expression:
    body1
else:
    body2
```


Пример:
```
point = int(input())

if abs(point) <= 25: # |point| <= 25
    print("Точка на отрезке!")
else:
    print("Точка отрезку не принадлежит!")
```