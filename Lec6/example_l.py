# Итерирование по ...

n = 10
for i in range(1, n):
    n += 1
    print("i is:", i)

print("Total n:", n)


a_set = set([1,2,3,4])
for num in a_set:
    a_set.add(num + 200)
    print("Elem:", num)