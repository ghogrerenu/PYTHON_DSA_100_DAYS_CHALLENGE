'''basic
q1Write a program to display a person's name, age and address in three different lines.
2.Write a program to swap two variables.
3.Write a program to convert a float into integer.
4.Write a program to take details from a student for ID-card and then print it in different lines.
5. Write a program to take an user input as integer then cony float.'''

# q1
print("Name - Renu")
print("Age - 21")
print("address - pune")

#q2 Write a program to swap two variables.
a = 8
b = 9
#swapping
a,b = b,a
print("After swapping a = ", a , "b = ", b)

# 3.Write a program to convert a float into integer.
a = 5.5
b = int(a)
print("After conversion " , b)

#4 Write a program to take details from a student for ID-card and then print it in different lines.
name = input("Enter student's name: ")
student_id = input("Enter student's ID: ")
course = input("Enter course name: ")

print("\n--- ID Card ---")
print("Name:", name)
print("ID:", student_id)
print("Course:", course)

#5 Write a program to take an user input as integer Convert user input (integer) to float:.
user = input("Enter integer : ")
print(float(user))