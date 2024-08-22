'''. Keep asking characters from user until he presses q on the keyboard.
Change all the capital letters to small, and all the small letters to capital.'''
def que():
    while True:
        s = input("Enter a character (press 'q' to quit): ")
        if s == 'q':
            break
        elif s.isalpha() and len(s) == 1:
            if s.islower():
                print(s.upper())
            else:
                print(s.lower())
        else:
            print("Please enter only one alphabetic character at a time.")

    print()  # To ensure a newline after the loop ends

# Call the function
que()
