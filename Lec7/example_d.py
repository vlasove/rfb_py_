# Сравнение строк
lhs_word = "abcd"
rhs_word = "abc"

print(lhs_word < rhs_word)
# ord(str) -> int, chr(int) -> str
# В Python все строки хранятся как unicode
# ASCII - сколько всего символов в стандарте
print("Code a is :", ord("a"))
print("Code is A:", ord("A"))
print("Code B is:", ord("B"))
print("Code Y is:", ord("Y"))

# for i in range(60, 150):
#     print(f"Character of {i}:", chr(i))

# Как сравниваются строки?
# "abcd"   <    "abc"
# 1)  ord("a")  ==   ord("a")
# 2)  ord("b")  ==   ord("b") 
# 3)  ord("c")  ==   ord("c")
# 4)  ord("d")  >>   А ТУТ НЕТ БУКВЫ :) -> False