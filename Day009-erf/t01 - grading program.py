# student_scores = { "name_of_student: "exam_score", }
student_scores = {
    "erfan": 18,
    "arshia": 12,
    "arman": 13,
    "ali": 14,
}

student_grades = {}

for student in student_scores:
    student_grades[student] = student_scores[student]

print(student_grades)