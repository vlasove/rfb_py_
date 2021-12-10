# Условный опретор с блоком else

#[-25, 25]

point = int(input())

if abs(point) <= 25: # |point| <= 25
    print("Точка на отрезке!")
else:
    print("Точка отрезку не принадлежит!")