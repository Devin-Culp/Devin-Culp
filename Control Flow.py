''' Student Grading Script '''

# Ask student for their mark

mark = int(input("Please enter your test mark (0-100)... "))

# Award correct grade

'''
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
'''

if mark >= 90:
    grade = "A"

elif mark >= 80:
    grade = "B"

elif mark >= 70:
    grade = "C"

elif mark >= 60:
    grade = "D"

else:
    grade = "F"

'''
elif = else if ... when the "if" statment doesn't work the "else"
'''

# Print grade to UI/console

if grade == "F":
    print("F")
else:
    print("Well done! you earned a grade of: " + grade)
#print(grade)
