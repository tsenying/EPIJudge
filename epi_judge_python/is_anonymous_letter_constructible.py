from test_framework import generic_test

from collections import Counter
def pythonic_is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    # 1. count occurrences of each character in letter
    # 2. count occurrences of each character in magazine_text
    # 3. constructible if number of occurrences in letter is less than equal to occurrences in magazine
    letter_counts = Counter(letter_text)
    magazine_counts = Counter(magazine_text)
    return not (letter_counts - magazine_counts)

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter_counts = Counter(letter_text)
    #
    for c in magazine_text:
        if c in letter_counts:
            letter_counts[c] -= 1
            if letter_counts[c] == 0:
                del letter_counts[c]
                if not letter_counts:
                    return True
    return not letter_counts

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
