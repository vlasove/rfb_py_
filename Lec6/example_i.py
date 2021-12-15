# Решение задачи E
n_days = int(input()) # Кол-во дней в семестре
general_student_set = set() # Множество студентов, которые были на всех занятияъ

for i in range(n_days):
    n_students_in_this_day = int(input()) # Студенты пришедшие в i день
    students_set = set() # Мн-во Студентов пришедших в i день
    for _ in range(n_students_in_this_day):
        student = input()
        students_set.add(student)

    if i == 0:
        general_student_set = general_student_set.union(students_set)
    else:
        general_student_set = general_student_set.intersection(students_set)

print(len(general_student_set))