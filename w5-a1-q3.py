'''Q3. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject which has marks
more than passing marks (above 33).'''

# Creating a dictionary with subjects and their marks
marks = {
    'Physics': 85,
    'Chemistry': 29,
    'Mathematics': 95,
    'Biology': 88,
    'English': 32
}

# Defining the passing marks
passing_marks = 33

# Iterating through the dictionary to find subjects with marks above passing marks
print("Subjects with marks above the passing marks are:")
for subject, mark in marks.items():
    if mark > passing_marks:
        print(subject,mark)
