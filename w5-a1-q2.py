"""Q2. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks
scored."""
# Creating a dictionary with subjects and their marks
marks = {
    'Physics': 85,
    'Chemistry': 90,
    'Mathematics': 95,
    'Biology': 88,
    'English': 78
}

# Finding the subject with the highest marks . The max function with key=marks.get finds the key (subject) with the highest value (marks).
max_subject = max(marks, key=marks.get)

# Printing the subject with the highest marks
print(f"The subject with the highest marks is {max_subject}.")
