# Решение задачи B
def solve(a,b,c):
    if a == 0:
        # bx + c = 0
        # x = -c/b
        if b == 0:
            return 0
        else:
            return 1
    else:
        # ax^2 + bx + c = 0
        d = b**2 -4*a*c
        if d > 0:
            return 2
        elif d == 0:
            return 1
        else:
            return 0

read_fh = open(file="input.txt", mode="r")
coeffs_str = read_fh.readline().strip()
read_fh.close()

coeffs = [float(coeff) for coeff in coeffs_str.split(sep = " ")]
print(coeffs)

result = solve(*coeffs) # solve(coeffs[0], coeffs[1], coeffs[2])


write_fh = open(file="output.txt", mode="w")
write_fh.write(str(result))
write_fh.close()