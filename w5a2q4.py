"""
Write a Python function that takes two dictionaries as input, where the
values are lists. The function should merge the lists corresponding to the
same keys in both dictionaries into a single list and return a new dictionary
with these merged lists
"""


def merge_dicts(dict1, dict2):
    merged_dict = {}  # Initialize empty dictionary

    # Combine keys from both dictionaries
    all_keys = set(dict1.keys()).union(dict2.keys())

    for key in all_keys:
        list1 = dict1.get(key, [])  # Get list from dict1 or empty list if key doesn't exist
        list2 = dict2.get(key, [])  # Get list from dict2 or empty list if key doesn't exist

        merged_dict[key] = list1 + list2  # Merge lists and assign to the new dictionary

    return merged_dict  # Return dictionary with merged lists


# Example usage
dict_a = {
    'fruits': ['apple', 'banana'],
    'vegetables': ['carrot']
}

dict_b = {
    'fruits': ['orange', 'grape'],
    'vegetables': ['broccoli', 'spinach'],
    'grains': ['rice', 'wheat']
}

result = merge_dicts(dict_a, dict_b)
print(result)
