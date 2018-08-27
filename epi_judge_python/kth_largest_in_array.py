from test_framework import generic_test

# e.g.
# 9	[-5, -3, -4, 8, -3, 0, -4, 1, 1]	-5	TODO
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
import random
def test_partition_around_pivot(A, left, right, pivot_index):
    pivot_value = A[pivot_index]
    new_pivot_index = left
    # swap pivot value out of the way during partitioning
    # it is swapped to new_pivot_index when partioning is done
    A[right], A[pivot_index] = A[pivot_index], A[right]
    for i in range(left, right):
        if A[i] > pivot_value:
            A[new_pivot_index], A[i] = A[i], A[new_pivot_index]
            new_pivot_index += 1
    # move pivot value to new_pivot_index
    A[new_pivot_index], A[right] = A[right], A[new_pivot_index]
    return new_pivot_index

def find_kth_largest(k, A):
    # TODO - you fill in here.
    # partition around pivot so that elements to left of pivot is greater than value at pivot
    # partition in place
    # pivot indexed value is the value for partitioning
    # return the index to partioned in place array where all elements to left of pivot is
    # greater than pivot value
    def partition_around_pivot(left, right, pivot_index):
        pivot_value = A[pivot_index]
        new_pivot_index = left
        # swap pivot value out of the way during partitioning
        # it is swapped to new_pivot_index when partioning is done
        A[right], A[pivot_index] = A[pivot_index], A[right]
        for i in range(left, right):
            if A[i] > pivot_value:
                A[new_pivot_index], A[i] = A[i], A[new_pivot_index]
                new_pivot_index += 1
        # move pivot value to new_pivot_index
        A[new_pivot_index], A[right] = A[right], A[new_pivot_index]
        return new_pivot_index
    #
    # partition repeatedly until len(A[p+1:]) == k-1
    left, right = 0, len(A) - 1
    while left <= right:
        pivot_index = random.randint(left, right)
        pivot_index = partition_around_pivot(left, right, pivot_index)
        if pivot_index < k - 1:
            left = pivot_index + 1
        elif pivot_index == k - 1:
            print('pivot_index=', pivot_index)
            return A[pivot_index]
        else:
            right = pivot_index - 1
    print('!!!!should not get here')
    return A[pivot_index]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
