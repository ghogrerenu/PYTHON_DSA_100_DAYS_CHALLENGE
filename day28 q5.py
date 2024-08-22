'''Q5. Ask a string from user. Replace all the space characters with “-”. Do not
use replace() method.
'''


def replace_spaces(s):
    # Use list comprehension to replace spaces with hyphens
    modified_list = ['-' if char == ' ' else char for char in s]

    # Join the list back into a string
    return ''.join(modified_list)


# Take user input for the string
user_input = input("Enter a string: ")

# Replace spaces with hyphens
modified_string = replace_spaces(user_input)

# Print the modified string
print("String after replacing spaces with hyphens:", modified_string)

