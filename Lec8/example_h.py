# Решение задачи N

n = int(input().strip())
numerics = [] # [100, 200, 300, 400]

for _ in range(n):
    numerics.append(int(input().strip()))

start_id = int(input().strip()) # 1
end_id = int(input().strip())   # 3

res = sum(numerics[start_id - 1: end_id]) # 100+200+300 = 600
print(res)