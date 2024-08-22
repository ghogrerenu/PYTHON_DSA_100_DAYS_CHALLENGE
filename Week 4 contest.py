'''Create a python function named isPalindrome which accepts a string
as a parameter and return True if its a palindrome. Palindrome are words
which is same when read from start and same when read from the end.'''


def isPalindrome(string):
    # Convert the string to lowercase to make the check case-insensitive
    string = string.lower()

    # Remove all non-alphanumeric characters from the string
    string = ''.join(filter(str.isalnum, string))

    # Check if the string is equal to its reverse
    return string == string[::-1]


# Example usage:
print(isPalindrome("racecar"))  # True
print(isPalindrome("hello"))    # False


# 2 nd way (user input)
def isPalindrome(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()

    # Remove all non-alphanumeric characters from the string
    s = ''.join(filter(str.isalnum, s))

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Get user input
user_input = input("Enter a word or phrase: ")

# Check if the input is a palindrome
if isPalindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')

