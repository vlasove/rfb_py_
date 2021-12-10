# Строки как базовый тип
name_str = "Bobby"
last_name_str = "Kotik"

# Конкатенация
res = name_str + " " + last_name_str # результат - новая строка!
print(res)

# Мультипликативная конкатенация (синтаксический сахар)
result = name_str * 5 # name_str + name_str + name_str + name_str + name_str
print(result) # Имеет смысл только при умножение на натуральное число


# Взятие длины
len_of_name = len(name_str * 2)
print("Len:", len_of_name)