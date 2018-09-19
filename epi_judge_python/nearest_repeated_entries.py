from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    # Option 1.
    # build hash table of words as keys and values as list of positions for each word
    # find least difference between positions, return word and distance
    # 
    # Option 2.
    # maintain hash table of word keys with values keeping last seen index
    # for each word calculate distance to last seen,
    #  if less than current shortest, then update shortest
    shortest = float('inf')
    words_last_index = {}
    for i, word in enumerate(paragraph):
        if word not in words_last_index:
            words_last_index[word] = i
        else:
            distance = i - words_last_index[word]
            if distance < shortest:
                shortest = distance
            words_last_index[word] = i
    return shortest if shortest != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
