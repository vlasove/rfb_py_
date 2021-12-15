# Решение задачи R

n = int(input())
words = set()

for _ in range(n):
    word = input()
    words.add(word)

new_word = input()

if new_word in words:
    print("НЕ ЗАСЧИТАНО")
else:
    print("ЗАСЧИТАНО")