"""Store name as a Key, and 5 marks in a List as a value in dictionary. Store
details of at least 5 students. Print only the total marks of every student in
ascending order."""
# Create the dictionary with student names as keys and marks as values (list)
students = {
    'Alice': [85, 90, 78, 92, 88],
    'Bob': [75, 80, 85, 70, 65],
    'Charlie': [95, 100, 92, 88, 96],
    'David': [60, 70, 65, 68, 72],
    'Eva': [80, 85, 82, 90, 87]
}

# Calculate total marks for each student and store in a new dictionary
total_marks_dict = {name: sum(marks) for name, marks in students.items()}

# Sort the total marks in ascending order and print them
sorted_total_marks = sorted(total_marks_dict.items(), key=lambda x: x[1])

# Print the total marks in ascending order
for name, total_marks in sorted_total_marks:
    print(f"{name}: {total_marks}")
