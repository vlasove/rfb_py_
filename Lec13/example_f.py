def sqrt_of_sum(first_val, second_val):
    return first_val**2 + second_val**3 - first_val*second_val**5

res = sqrt_of_sum(1, 10)  # результат -98999
print(res)

res2 = sqrt_of_sum(10, 1) # результат 91
print(res2)

res3 = sqrt_of_sum(second_val = 10, first_val = 1) # arg naming
print(res3)

