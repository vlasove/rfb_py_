# Решение задачи O

n = int(input()) 
res = 0
############################ 1-ый вариант
# 1 - 2 + 3 - 4 + 5
for i in range(n):
    numeric = int(input())
    if i % 2 ==0:
        res += numeric
    else:
        res -= numeric

print(res)

res = 0
####################### 2-ой вариант
for i in range(n):
    numeric = int(input())
    res += numeric * (-1) ** i

print(res)