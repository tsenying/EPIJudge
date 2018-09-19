from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    # iterate through both arrays concurrently and look for matches
    intersect = [] # common elements in both arrays, no duplicates
    a, b = 0, 0 # ptrs into A, B
    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            if not intersect:
                intersect.append(A[a])
            elif intersect[-1] != A[a]:
                intersect.append(A[a])
            a += 1
            b += 1
        elif A[a] < B[b]:
            a += 1
        else:
            b += 1
    return intersect


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
