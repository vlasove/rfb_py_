## Лекция 2. Работа с I/O

* Работа с потоком ввода (Input Stream, STDIN)
* Работа с потоком вывода (Output Stream, STDOUT)

### 1. Выходной поток
* В `Python` существует команда (функция), которая выводит все свои аргументы в выходной поток (по умолчанию `STDOUT` == `cmd`). Команда `print(...)`.
* Пример:
```
print("Hello World!")
```

* Многострочный вывод
```
print("Hello World!")
print("I am uber programmer!")
```

* Каждый print() выводит информация на отдельной строке потому что по умолчанию, после вывода своего аргумента `print()` допишет вам `\n`

* Вывод нескольких значений в одной команде:
```
first_person_name = "Bob"
second_person_name = "Alice"

print(first_person_name, second_person_name, "Alex", 100500)
```
* При передаче аргументов команде `print()` значения располагаются в выходном потоке , разделенные (по умолчанию) пробелом!

* Иногда помогает форматирование строки перед выводом в STDOUT:
```
# 3. Форматированный вывод (форматирование строк или f-strings)
drink = "Water"
dish = "Broccoli"
message = f"I'm Bob, and I like '{drink}' and {dish}" # Работает только с 3.7 и выше
# message = "I'm Bob, and I like {}".format(drink) Работает и в старых версиях
print(message)
```

### 2. Входной поток STDIN
* В `Python` есть функция `input()` - которая по умолчанию обрабатывает входной поток.
```
name = input() # "Alice and Bob"
print(f"Hello, It's {name}")
```

* Считывание нескольких значений
```
# Считывание нескольких значений
name = input()
last_name = input()
age = input()

message = f"Имя: {name} , Фамилия: {last_name} , Возраст: {age} . Студент BPS"
print(message)
```

#### 2.1 Как не надо сдавать задачи в тестовую систему
* Деды в школах и универах учат, что нужно всегда печатать т.н. "приглашение на ввод".
```
# Считывание нескольких значений
name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
age = input("Введите возраст: ")

message = f"Имя: {name} , Фамилия: {last_name} , Возраст: {age} . Студент BPS"
print(message)
```
* Но они забывают сказать, что это приглашение засоряет выходной поток программы!