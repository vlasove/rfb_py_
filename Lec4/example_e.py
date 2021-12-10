# if expression1:
#     body1
# elif expression2:
#     body2
# elif expression3:
#     body3
# ...
# else:
#     body_else

# Пользователь вводит 2 ЦЕЛЫХ числа
# и знак + или -
# в случае, если введеной любой другой знак - пишем "Данный функционал не поддерживается"

a_int = int(input())
b_int = int(input())
sign = input()

if sign == "+":
    print(a_int + b_int)
elif sign == "+": # Пример дублирующегося условия (не будет выоплнено никогда!)
    print(2*(a_int + b_int))
elif sign == "-":
    print(a_int - b_int)
else:
    print("Данный функционал не поддерживается")