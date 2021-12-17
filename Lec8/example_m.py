# Решение задачи P
n_general_dishes = int(input().strip())
general_dishes = []
prepared_dishes = set()

for _ in range(n_general_dishes):
    general_dishes.append(input().strip())

n_days = int(input().strip())

for _ in range(n_days):
    n_dish_per_day = int(input().strip())
    for _ in range(n_dish_per_day):
        dish = input().strip()
        prepared_dishes.add(dish)

for dish_to_delete in prepared_dishes:
    if dish_to_delete in general_dishes:
        general_dishes.remove(dish_to_delete)

for dish_to_stdout in sorted(general_dishes):
    print(dish_to_stdout)