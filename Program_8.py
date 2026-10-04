def calculate_statistics(*grades):
    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    return minimum, maximum, average

def grade_distribution(*grades):
    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return distribution

def student_performance(**students):
    for name, grade in students.items():
        if grade >= 90:
            letter = "A"
        elif grade >= 80:
            letter = "B"
        elif grade >= 70:
            letter = "C"
        elif grade >= 60:
            letter = "D"
        else:
            letter = "F"

        print(name, ":", grade, "->", letter)

grades = (95, 82, 76, 68, 89, 91, 55, 73)

minimum, maximum, average = calculate_statistics(*grades)

print("Student Grades:")
print(grades)

print("\nMinimum Grade:", minimum)
print("Maximum Grade:", maximum)
print("Average Grade:", round(average, 2))

distribution = grade_distribution(*grades)

print("\nGrade Distribution:")
for grade, count in distribution.items():
    print(grade, ":", count)

print("\nIndividual Student Performance:")
student_performance(
    Rahul=95,
    Aman=82,
    Priya=76,
    Neha=68,
    Riya=89
)