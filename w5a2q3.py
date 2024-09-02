""""
Write a Python function that takes a dictionary as input where the
values are lists of integers. The function should return a new dictionary
where the values are lists containing only the even integers from the
original lists.
"""


def filter_even_numbers(input_dict):
    even_dict = {}  # Initialize empty dictionary

    for key, value_list in input_dict.items():
        even_dict[key] = [num for num in value_list if num % 2 == 0]  # Filter even numbers

    return even_dict  # Return dictionary with even numbers


# Example usage
sample_dict = {
    'list1': [1, 2, 3, 4],
    'list2': [10, 11, 12, 13],
    'list3': [20, 21, 22, 23]
}

result = filter_even_numbers(sample_dict)
print(result)
