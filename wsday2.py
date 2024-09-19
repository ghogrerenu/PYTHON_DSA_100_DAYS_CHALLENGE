'''Problems

1. Write a program to check if a number is positive.

2. Write a program to check whether a number is odd or even.

3. Write a program to create area calculator.

4. Write a program check whether the passed letter is a vowel or not.
5 Check if a number is 1-digit, 2-digit, up to 5-digits:'''

#1. Write a program to check if a number is positive.
number = 5
if number > 0:
    print("it is positive no")
else:
    print("it is negative no")

#2. Write a program to check whether a number is odd or even.
number = 5
if number % 2 == 0:
    print("it is even no")
else:
    print("it is odd no")

#3. Write a program to create area calculator.
a = int(input("enter no : "))
b = a**2
print(b)

# Check if the letter is a vowel:
letter = 'a'
vowels = 'aeiouAEIOU'
if letter in vowels:
    print("The letter is a vowel.")
else:
    print("The letter is not a vowel.")

# Check if a number is 1-digit, 2-digit, up to 5-digits:
number = 456

if 0 <= number <= 9:
    print("Single digit number.")
elif 10 <= number <= 99:
    print("Two digit number.")
elif 100 <= number <= 999:
    print("Three digit number.")
elif 1000 <= number <= 9999:
    print("Four digit number.")
elif 10000 <= number <= 99999:
    print("Five digit number.")
else:
    print("Number has more than 5 digits.")

