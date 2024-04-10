# Exercise 1
# Grading Program.

# DON'T CHANGE THE CODE BELOW
student_score = {
    "harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}


# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
student_grades = {}

for student in student_score:
    score = student_score[student]

    if score >= 91 and score <= 100:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectation"
    elif score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
# ------------------------------------------------------------------------------------------------------------------------------------------
