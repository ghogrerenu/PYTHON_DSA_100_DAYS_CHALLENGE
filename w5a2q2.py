"""Q2. Create a function named countChar which will accept a string as a
parameter. Create a dictionary having frequency of each character."""


def countChar(input_string):
    char_frequency = {}  # Initialize empty dictionary

    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1  # Increment count if char exists
        else:
            char_frequency[char] = 1  # Add new char with count 1

    return char_frequency  # Return dictionary with char frequencies


# Example usage
result = countChar("hello world")
print(result)



