for i in range(1, 101):
    if i % 2 == 0:
        continue
    if i % 13 == 0:
        break
    print(i)