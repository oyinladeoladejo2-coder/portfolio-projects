def student_grade(score):
    if score >= 100:
        return "Error: score cannot be above 100 "
    if score >= 70 :
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],
    ["oyin", 65, 80, 50],
    ["david", 100, 100, 100]
]

for student in students:
    name = student[0]

    total = 0

    for score in student[1:]:
        total += score

    average = total / 3
    grade = student_grade(average)

    print(f"{name} - Average: {average:.2f} - Grade: {grade}")
