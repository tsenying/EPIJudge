from test_framework import generic_test

def find_first_greater_than_k(tree, k):
    # TODO - you fill in here.
    # descend tree until possibilities exhausted
    first = None
    while tree:
        if tree.data > k:
            first = tree
            # check left to see if anything smaller
            tree = tree.left
        else:
            # tree.data <= k
            # no point looking left
            tree = tree.right
    return first


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
