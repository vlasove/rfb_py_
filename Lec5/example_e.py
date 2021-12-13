count = 0

while True:
    numeric = int(input())
    if numeric < 0:
        break

    if numeric % 2 ==0:
        count += 1 # count = count + 1
        # count -= 1 # count = count - 1
        # count *= 2 # count = count * 2
        # count /= 3 # count = count / 3
        # count **= 10 # count = count ** 10
        # count //= 3 # count = count // 3
        # count %= 7 # count = count % 7

print("Count is:", count)