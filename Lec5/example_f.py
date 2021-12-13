CURRENT_MAX = -1000000
CURRENT_MIN = 10 ** 10

while True:
    numeric = int(input())
    if numeric < 0:
        break

    if numeric > CURRENT_MAX:
        CURRENT_MAX = numeric

    if numeric < CURRENT_MIN:
        CURRENT_MIN = numeric

print("Current max:", CURRENT_MAX)
print("Current min:", CURRENT_MIN)