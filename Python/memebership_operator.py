# Memebership operators = used to test whether a value or variable is found
#                         in a sequence (string, sets, tuple, list, dictionary)
#                         1. in
#                         2. not in

studentGrades = {"Sandy":"A",
                 "Squidward":"B",
                 "Spongebob":"C",
                 "Patrick":"D"}

student = input("Enter the name of the student: ")

if student in studentGrades:
    print(f"{student}'s grade is {studentGrades[student]}")
else:
    print(f"{student} is not found!")

# if student not in studentGrades:
#     print(f"{student} is not found!")
# else:
#     print(f"{student}'s grade is {studentGrades[student]}")

