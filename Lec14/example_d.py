# Факториал
# n! = (n) * (n-1) * (n-2) * ... (1)
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 4! = 4 * 3 * 2 * 1 = 24
# 1! = 1
# 0! = 1
def factorial(n):
    res = 1
    if n <= 1:
        return res
    for i in range(2, n+1):
        res *= i
    return res


def main():
    n = int(input().strip())
    #if type(n) == int:
    for i in range(n+1):
        print(f"{i}! = {factorial(i)}")
    
main()