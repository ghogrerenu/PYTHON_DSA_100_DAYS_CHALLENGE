"""Store name as a Key, and 5 marks in a List as a value in dictionary. Store
details of at least 5 students. Print the total marks with percentage of each
and every student."""
# Dictionary with student names as keys and list of 5 marks as values
students = {
    'Alice': [85, 90, 78, 92, 88],
    'Bob': [75, 80, 85, 70, 90],
    'Charlie': [65, 70, 75, 80, 85],
    'David': [95, 88, 92, 85, 90],
    'Eva': [80, 85, 88, 90, 92]
}

# Calculate and print total marks and percentage for each student
for name, marks in students.items():
    total = sum(marks)  # Total marks
    percentage = (total / 500) * 100  # Percentage out of 500
    print(f"{name}: Total Marks = {total}, Percentage = {percentage:.2f}%")
