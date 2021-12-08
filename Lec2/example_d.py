# 0. Вывод без переменных
print("Alice")

# 1. Вывод через переменную
name = "Bob"
print(name)

# 2. Вывод нескольких значений в одной команде
first_person_name = "Bob"
second_person_name = "Alice"

print(first_person_name, second_person_name, "Alex", 100500)

# 3. Форматированный вывод (форматирование строк или f-strings)
drink = "Water"
dish = "Broccoli"
message = f"I'm Bob, and I like '{drink}' and {dish}" # Работает только с 3.7 и выше
# message = "I'm Bob, and I like {}".format(drink) Работает и в старых версиях
print(message)