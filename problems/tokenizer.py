"""
Exercise: Simplified Tokenizer
Goal: Create a tokenizer that splits a sentence into a list of words.
"""


SCRYPT_RANDOM_SENTENCES = [
    "I love you",
    "You like me",
    "Flowers love sun",
    "I love flowers",
    "Some flowers are red",
    "Some flowers are blue",
    "Sun is yellow",
    "Sun is hot",
    "I like hot coffee",
    "Love is red",
    "Eating potatoes everyday",
    "I like potatoes",
]

scrypt_tokenized_sentences = []
for sentence in SCRYPT_RANDOM_SENTENCES:
    tokenized_sentence = sentence.split()
    scrypt_tokenized_sentences.append(tokenized_sentence)

print(
    "Tokenized sentences : \n",
    scrypt_tokenized_sentences
)