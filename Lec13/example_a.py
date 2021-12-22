#
def my_function():
    print("Hello", "Bob!")
    print("Bob", "is 17 years old")


my_function()
i = 0
while True:
    i+=1
    if i > 10:
        break
    else:
        my_function()


print("Done")
my_function()