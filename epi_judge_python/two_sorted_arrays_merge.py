from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    # TODO - you fill in here.
    # m = number of integers in A
    # n = number of integers in B
    # merge the two arrays into A backwards,
    #  starting at position m+n-1
    a, b = m-1, n-1
    last = m + n - 1
    print("a={},b={},last={},A={},B={}".format(a,b,last,A,B))
    while a >=0 and b >=0:
        # print('while last={},a={},b={},A[a]={},B[b]={}'.format(last,a,b,A[a],B[b]))
        if A[a] >= B[b]:
            # print('A[a] >= B[b]')
            A[last] = A[a]
            a -= 1
        else:
            # print('A[a] < B[b]')
            A[last] = B[b]
            b -= 1
        last -= 1
        # print('A=',A)
    # if n > m, move remainder of B
    # print("a={},b={},last={},A={}".format(a,b,last,A))
    if b >= 0:
        A[0:b+1] = B[0:b+1]
        print("b >= 0, b={}, B[0:b+1]={}, A={}".format(b, B[0:b+1], A))
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
