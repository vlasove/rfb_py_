# Строковый метод .split()
message = "Bob likes Python programming"
words = message.split(sep=" ")
print("Words:", words)

# Строковый метод .join()
output_str = ", ".join(words) # "Bob" + "\n" + "likes" + "\n" + "Python" +\n" + "programming"
print(output_str)

# .join() работает только с list[str]
nums = [10, 20, 30]
for i in range(len(nums)):
    nums[i] = str(nums[i])

print(", ".join(nums))
