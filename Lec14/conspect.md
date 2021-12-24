## Лекция 14. Виды аргументов функций

* `Required Positional Args` 
* `Default Value Args`
* `Variadic Args`


### 1. RP аргументы
* Пример:
```
def add(a, b):
    return a**2 + b**3 - 2*a*b*6
```
* Порядок следования аргументов важен!
```
print(add(2, 10))
print(add(10, 2))
```

* Через явное обращение в аргументам можно порядок менять
```
print(add(b = 23, a = 1))
```


* Свойство необходимости RP аргументов
```
# add(2) # Не хватает аргументов
add(2,2)
# add(2,2,2) # Слишком много аргументов
```

### 2. Default Value аргументы
* Аргументы со значением по умолчанию - проставляем значения на жтапе определения функции
```
def add(a = 3, b = 4):
    return a + b


print("10 + 20 = ", add(10, 20))
print("10 + ? = ", add(10))
print("? + ? = ", add())
```

* Частичное переопределение значений по умолчанию
```
def add(a = 3, b = 4, c = 5):
    return a ** 2 - b ** 3 + c ** 5

add(b = 10)
```

* В примере выше при вызове функции `add` переопределим значение b, а все остальные аругменты остаются такими же, как и в сигнатуре функции (при определении функции).

* Смешивание с `rp` аругментами:
```
def sqrt_differnce(a, b, c = 1, d = 1):
    return (a +b) ** 2 - (c - d) ** 2

print(sqrt_differnce(2,3,4,5))
print(sqrt_differnce(5,5))
```

### 3. Variadic аргументы
* Континуальные аргументы. Бывают двух типов - приводимые в кортеж и приводимые в словарь
* Континуальный аргумент (приводимый к кортежу):
```
def add(*args):
    res = 0
    for arg in args:
        if arg % 2 == 0:
            res += arg**2
        else:
            res += arg**3
    return res

```
* При вызове функции `add` все переданные ей аргументы будут сложены в кортеж с именем `args`.
* Имя `args` - не стандартное (можно выбрать любое), но это договоренность между разработчиками `Python`

* Континуальный аргумент (приводимый к словарю)
```
def build_map(**kwargs):
    """
    kwargs - key-word args
    """
    print("Len:", len(kwargs))
    print("Type:", type(kwargs))
    print("Value:", kwargs)
```

* При вызове функции `build_map` передаем набор пар (key_word_name = arg, ....). После чего все пары будут представлены в словаре `kwargs = {"key_word_name" : arg, }`.

* Смешивание континуальных аругментов
```
def mutant(*args, **kwargs):
    print(args)
    print(kwargs)

```