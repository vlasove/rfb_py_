# if expression:
#     body

age = int(input())

if age >= 18:
    print("Your age is:", age)
    print("Welcome to our service!")
    print("Press here to continue!")
    if True: # Вложенный условный оператор
        print("Internal if body")
        if True:
            print("Sub-internal body")

print("Service done!")