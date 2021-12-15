# Решение задачи S.

from_home_to_park = set()
while True:
    message = input()
    if message == "":
        break
    from_home_to_park.add(message)


from_park_to_home = set()
while True:
    message = input()
    if message =="":
        break
    from_park_to_home.add(message)

result = from_home_to_park.intersection(from_park_to_home)
print(len(result))