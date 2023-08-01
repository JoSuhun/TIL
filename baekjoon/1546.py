num = int(input())

grades = list(map(int, input().split()))
MAX = max(grades)

new_grades = []

for grade in grades:
    new_grades.append(grade/MAX*100)

print(sum(new_grades)/num)
