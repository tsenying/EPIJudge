from test_framework import generic_test

import collections
def can_form_palindrome(s):
    # TODO - you fill in here.
    # collections.Counter(s) counts occurrences of characters 'edified' => Counter({'e': 2, 'd': 2, 'i': 2, 'f': 1})
    # collections.Counter(s).values() extracts just the counts => dict_values([2, 2, 2, 1])
    # possibility for palindrome if all counts are even except for 1 (odd length string)
    #   so modulus % 2 of counts should all be 0 except at most 1 odd character
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
