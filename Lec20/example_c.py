"""
Построчное чтение из файла
"""
fh = open(file="input.txt", mode="r")

line = fh.readline()
line_num = 1
while line != "":
    print(f"Num:{line_num}, Content: {line.strip()}")
    line_num += 1
    line = fh.readline()


fh.close()