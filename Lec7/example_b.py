# Решение задачи H
yes_words = set(["да" , "Да" , "дА", "ДА", "ад", "аД", "Ад", "АД"])

word = input()

if (word[0] + word[-1]) in yes_words:
    print("СОГЛАСЕН")
else:
    print("НЕ СОГЛАСЕН")