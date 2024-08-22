'''Q4. Write a Python program to generate and print a dictionary that
contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.'''

# Function to generate the dictionary
def generate_square_dict(n):
    square_dict = {x: x*x for x in range(1, n+1)}
    return square_dict

# Set the value of n
n = 5

# Generate the dictionary and print it
result = generate_square_dict(n)
print(result)

