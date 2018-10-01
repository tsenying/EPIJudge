from test_framework import generic_test


def x_intersect_two_sorted_arrays(A, B):
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

def intersect_two_sorted_arrays(A, B):
    # advance through arrays concurrently
    intersect = list()
    # maintain pointers into A, B
    a, b = 0, 0
    # print('a={}, A[a]={}, b={}, B[b]'.format(a,A[a],b,B[b]))
    while a < len(A) and b < len(B):
        print('a={}, A[a]={}, b={}, B[b]={}'.format(a,A[a],b,B[b]))
        if A[a] == B[b]:
            intersect.append(A[a])
            a, b = a + 1, b + 1
            while a < len(A) and A[a] == A[a - 1]:
                a += 1
            while b < len(B) and B[b] == B[b - 1]:
                b += 1
            print('A[a] == B[b], a={}, b={}, intersect={}'.format(a, b, intersect))
        elif A[a] < B[b]:
            while a < len(A) and A[a] < B[b]:
                a += 1
                print('A[a] < B[b] a=', a)
        else:
            while b < len(B) and A[a] > B[b]:
                b += 1
                print('A[a] > B[b] b=', b)
    print('!!! intersect=', intersect)
    return intersect

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
