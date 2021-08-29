student_score = int(input())
max_score = int(input())

student_score_percent = student_score * 100 / max_score

if student_score_percent >= 90.0:
    print("A")
elif student_score_percent >= 80.0:
    print("B")
elif student_score_percent >= 70.0:
    print("C")
elif student_score_percent >= 60.0:
    print("D")
else:
    print("F")
