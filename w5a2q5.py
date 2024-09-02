"""
. Write a Python program to combine two dictionary by adding values
for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""


def combine_dictionaries(d1, d2):
    combined_dict = {}  # Initialize empty dictionary

    # Combine keys from both dictionaries
    all_keys = set(d1.keys()).union(d2.keys())

    for key in all_keys:
        combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)  # Add values from both dictionaries

    return combined_dict  # Return the combined dictionary


# Example usage
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = combine_dictionaries(d1, d2)
print(result)
