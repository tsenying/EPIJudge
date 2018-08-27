from test_framework import generic_test

def binary_search(A, k):
    L, U = 0, len(A) - 1
    while L <= U:
        M = ((U - L) // 2) + L
        if k < A[M]:
            U = M - 1
        elif k == A[M]:
            return M
        else:
            L = M + 1
    return -1

# e.g.
# A = [1, 1, 2, 3, 4, 5, 6, 7], k = 1, return = 0 (not 1)
def search_first_of_k(A, k):
    # TODO - you fill in here.
    # 0. set not found lower and upper bounds
    # 1. do binary search
    # 2. if found:
    # 3.   binary search left: while found, set lower found index
    # 4.   binary search right: while found, set upper found index
    found_index = binary_search(A, k)
    #
    lower_found_index = found_index
    while lower_found_index != -1:
        found_index = lower_found_index
        lower_found_index = binary_search(A[:found_index],k)
    return found_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
