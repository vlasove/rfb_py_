"""
Считывание всех строк в виде списка
"""

fh = open(file="input.txt", mode="r")
lines = fh.readlines()
for line in lines:
    print(line.strip())
fh.close()