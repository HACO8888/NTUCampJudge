from functools import cmp_to_key

input()
students = input()

students = students.split(" ")
students.sort(key=cmp_to_key(lambda a, b: int(a) - int(b)))

print(students[-1])