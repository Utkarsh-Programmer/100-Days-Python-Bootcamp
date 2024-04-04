# Exercise 2
# High Score.

# DON'T CHANGE THE CODE ABOVE
student_score = input("Enter student heights(cm) : ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
high_score = 0

for score in student_score:
    if score > high_score:
        high_score = score

print(f"High Score: {high_score}")
# ------------------------------------------------------------------------------------------------------------------------------------------
