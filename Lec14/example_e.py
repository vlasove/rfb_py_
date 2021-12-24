def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 5!
# factorial(5) -> 120
#                120                                  

def main():
    n = int(input().strip())
    #if type(n) == int:
    for i in range(n+1):
        print(f"{i}! = {factorial(i)}")
    print(factorial(995))
    
main()