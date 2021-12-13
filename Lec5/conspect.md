## Лекция 5. Циклы

В `Python` существует 2 конструкции циклов:
* `while` (`while-do`) - который позволяет запускаться в "условно-бесконечном режиме"
* `for` (`range based for`)

**Цикл** - локальный участок кода, который выполняется заранее известное количество раз(или до заранее известного события).

### 1. Синтаксис while
```
while expression:
    body
```

### 1.1 Простейший while True
* Для остановки итерирования цикла `while True` используем ключевое слово `break`
* `break` - при выполнении прерывает текущую итерацию (текущее выполнение тела цикла) и передает управление первой инструкции стоящей ЗА ПРЕДЕЛЕАМИ тела цикла.
```
# Условно-бесконечный while и первое ключевое слово break
while True:
    numeric = int(input())
    if numeric >= 100 and numeric % 2 ==0:
        print("It's over")
        break
    print("Current numeric:", numeric)

print("Out of while body")
```

* `continue` - при выполнении прерывает текущую итерацию (текущее выполнение тела цикла) и передает управление СЛЕДУЮЩЕЙ ИТЕРАЦИИ ЦИКЛА.
```
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
```

### 2. Синтаксис for

