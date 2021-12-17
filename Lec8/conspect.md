## Лекция 8. Коллекции. Списки

**Список** (list) - упорядоченная (индексирумеая) коллекция, способная хранить элементы любого типа.


### 1. Инициализация
```
# Инициализация списка
a_list = []
b_list = list()

print("b_list origin:", b_list)
print("a_list type :", type(a_list))
print("b_list len :", len(b_list))

numeric_list = [10, 20, 30, 40, 50]
something_list = [numeric_list, "ASDG", "bob", 100500, set([1,2,3])]

print(numeric_list)
print(something_list)
```

* Наполнение списка
```
# Наполенение списка
numerics = []

# Добавление в конец
numerics.append(10)
numerics.append(20)
numerics.append(30)

print(numerics)

# Добавление в начало (или проивзольное место)
numerics.insert(0, 99)
numerics.insert(2, 9999999)
print(numerics)
```

### 2. Индексация, срезы, итерирование, сравнение, обработка
* Индексация списков
```
# Индексация
nums = [10, 20, 30, 40, 50]
print("First elem:", nums[0])
print("Second elem:", nums[1])
print("Last elem:", nums[-1])

# Итерирование по индексу
for i in range(len(nums)):
    print(f"Id:{i} Elem:{nums[i]}")
```

* Срезы
```
# Срезы
nums = [10, 20, 30, 40, 50]
print("Slice:", nums[1:4])
print("Reversed:", nums[::-1])
print("Each 2:", nums[::2])

sl = nums[::2]
for i in range(len(sl)):
    print(f"Id:{i} Elem:{sl[i]}")
```

* Итерирование `for-each`
```
# Итерирование по элементам
nums = [10, 20, 30, 40, 50]

for n in nums[::2]:
    print("Elem:", n)
```

* Сравнение (точно такое же как и у строк - поэлементное)
```
# Сравнение списков
first = [10, 20, 30]
second = [10, 20, 31]

print("==", first == second)
print("!=", first != second)
print("<", first  < second)
```

* Стандартная обработка списков
```
# Обработка списков
nums = [ 10, 20, 30, 40, 50]

# Проверка вхождения
if 20 in nums:
    print("20 in nums")

# Изменение списка
nums[0] = 100500
print(nums)

# min/max/sum
print("sum:", sum(nums))
print("max:", max(nums))
print("min:", min(nums))
```