'''q3. Python Program to remove all duplicates from a given string.'''


def dup(s):
    # Initialize an empty string to store the result
    result = ""
    # Create a set to track characters that have been seen
    seen = set()

    # Iterate over each character in the input string
    for i in s:
        # Check if the character has not been seen before
        if i not in seen:
            # Append the character to the result string
            result += i
            # Add the character to the set of seen characters
            seen.add(i)

    # Return the resulting string with duplicates removed
    return result


# Take user input
u = input("Enter string: ")

# Remove duplicates from the user input
v = dup(u)

# Print the string after removing duplicates
print("String after removing duplicates:", v)

