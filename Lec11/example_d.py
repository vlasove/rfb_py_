num_tuple = (10, 20, 30, 40 ,50)
#num_tuple[0] = 100 # Не получится - кортеж не изменяемый!

nums = [0] * 10000
nums_tuple = (0,) * 10000
print("Nums List size :", nums.__sizeof__(), "bytes")
print("Nums Tuple size:", nums_tuple.__sizeof__(), "bytes")