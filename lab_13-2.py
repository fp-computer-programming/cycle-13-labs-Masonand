
#create the dictionary for grades
grades = {
    'Assignment 1': 85,
    'Quiz 1': 78,
    'Midterm': 92,
    'Project': 88,
    'Assignment 2': 95,
    'Quiz 2': 65,
    'Final': 90,
    'Participation': 100,
    'Assignment 3': 45,  #Example of a grade below 50
    'Quiz 3': 55  #Example of a grade between 50 and 70
}

#print all needed grades recieved
print("Grades received:", [grade for grade in grades.values()])

#Printing the name of each assignment
for assignment in grades:
    print(assignment)

#Printing the name and grade for each assignment with a grade of 70 or above
for assignment, grade in grades.items():
    if grade >= 70:
        print(f"{assignment}: {grade}")

for assignment, grade in grades.items():
    if grade <= 50:
        print(f"{assignment}: {grade}")
