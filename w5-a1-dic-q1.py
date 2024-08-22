'''Q1. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the highest marks scored.'''
# Create a dictionary with subjects and their corresponding marks
marks = {
    "Physics": 85,
    "Chemistry": 90,
    "Mathematics": 95,
    "Biology": 88,
    "English": 92
}

# Find the subject with the highest marks
highest_marks = max(marks.values())

# Print the highest marks scored
print(f"The highest marks scored are: {highest_marks}")
