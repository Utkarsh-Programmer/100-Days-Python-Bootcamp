# Exercise 1
# Average Height.

# DON'T CHANGE THE CODE ABOVE
student_heights = input("Enter student heights(cm) : ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
number_of_students = len(student_heights)

sum_of_heights = 0
for height in student_heights:
    sum_of_heights += height

average_height = round(sum_of_heights/number_of_students)

print(f'Average Height: {average_height} cm.')
# ------------------------------------------------------------------------------------------------------------------------------------------
