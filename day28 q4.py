'''. Ask a sentence from user. Then ask a integer k from user. Print all the
words which are greater or equal to k.'''


def filter_words_by_length(sentence, k):
    # Split the sentence into words
    words = sentence.split()

    # Filter words based on their length
    filtered_words = [i for i in words if len(i) >= k]

    return filtered_words


# Take user input for the sentence
sentence = input("Enter a sentence: ")

# Take user input for the integer k
k = int(input("Enter an integer k: "))

# Get the words with length greater than or equal to k
result = filter_words_by_length(sentence, k)

# Print the filtered words
print("Words with length greater than or equal to", k, "are:", result)


