# При смешивание rp аргументов и опциональных (с значением по умолчанию)
# аргументы с значением пишутся ВСЕГДА ПОСЛЕ RP аргументов!!!!!!!!!!!!
def sqrt_differnce(a, b, c = 1, d = 1):
    return (a +b) ** 2 - (c - d) ** 2

print(sqrt_differnce(2,3,4,5))
print(sqrt_differnce(5,5))