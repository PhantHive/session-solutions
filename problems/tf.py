"""
Exercise: Frequency Matrix
Goal: Create a frequency matrix from a list of sentences (strings)
A frequency matrix is a matrix where each row is a sentence and each column is a word.
The value of each cell is the number of times the word appears in the sentence.
"""

SCRYPT_RANDOM_SENTENCES = [
    "True it's false",
    "Ok I eat  potatoes",
    "True it's false",
]


def term_frequency():
    unique_words = {}
    for sentence in SCRYPT_RANDOM_SENTENCES:
        for word in sentence.split():
            if word not in unique_words:
                unique_words[word] = 0
            unique_words[word] += 1

    return unique_words


def term_frequency_matrix():
    unique_words = term_frequency()
    matrix = []
    for sentence in SCRYPT_RANDOM_SENTENCES:
        row = []
        for word in unique_words:
            row.append(sentence.count(word))
        matrix.append(row)
    return matrix


print(f"unique_words: {term_frequency()}")
print("matrix:")
for row in term_frequency_matrix():
    print(row)
