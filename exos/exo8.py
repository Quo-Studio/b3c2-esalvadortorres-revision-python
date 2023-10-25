
grades = {
    "Tibz": 85,
    "Pierre": 92,
    "Charlie": 78,
    "Francois": 90,
    "Sarah": 87
}

maximum = max(grades.values())

for student, grade in grades.items():
    if grade == maximum:
        print(f"{student} a la meilleure note de : {maximum}")
        break
