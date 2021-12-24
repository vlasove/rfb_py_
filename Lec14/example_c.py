# Принимает число n - целое,
# если n <= 0 - возвращает []
# если n > 0 - возвращает список длины n - первые n элементов
# последовательности Фибоначчи
def fibonacci_generator(n):
    if n <= 0:
        return []
        
    elems = []
    first, second = 1, 1

    if n == 1:
        elems.append(first)
        return elems
    elif n == 2:
        elems.append(first)
        elems.append(second)
        return elems
    else:
        elems = [first, second]
        for _ in range(n -2):
            first, second = second, first + second
            elems.append(second)
        return elems

def main():
    n = int(input().strip())
    fib_elems = fibonacci_generator(n)
    for id in range(len(fib_elems)):
        print(f"Id {id}, Elem: {fib_elems[id]}")



main()