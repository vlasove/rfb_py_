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