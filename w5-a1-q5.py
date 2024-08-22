'''Q5. Write a Python program to check if a dictionary is empty or not.'''
# Define the dictionary
my_dict = {}

# Check if the dictionary is empty
if len(my_dict) == 0:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")


# way 2
# Define the dictionary
my_dict = {}

# Check if the dictionary is empty
if not my_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")
