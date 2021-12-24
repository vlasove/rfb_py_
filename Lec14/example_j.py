def add(*args):
    res = 0
    for arg in args:
        if arg % 2 == 0:
            res += arg**2
        else:
            res += arg**3
    return res


print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3,4,5,6,7,8,9))
print(add(1,1,1,1,1,11,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11))
