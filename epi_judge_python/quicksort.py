from test_framework import generic_test

A=[2,3,1]
def partition(A, lo, hi):
    print('partition: A={},lo={},hi={}'.format(A,lo,hi))
    i = lo # A for index < i is less than pivot value
    j = hi # A for index > j is greater than pivot value
    pivot_value = A[(hi-lo)//2 + lo]
    print('partition pivot_value=', pivot_value)
    while True:
        while A[i] < pivot_value:
            i += 1
        while A[j] > pivot_value:
            j -= 1
        if i >= j:
            print('partition i={}, j={}, return={}'.format(i,j,i))
            return i
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

import random
def partition_from_exercise_11_8(A, left, right):
    print('partition: A={},left={},right={}'.format(A,left,right))
    # pivot_index = random.randint(left, right)
    pivot_index = (len(A)-1)//2
    pivot_value = A[pivot_index]
    new_pivot_index = left
    # swap pivot value out of the way during partitioning
    # it is swapped to new_pivot_index when partioning is done
    A[right], A[pivot_index] = A[pivot_index], A[right]
    for i in range(left, right):
        if A[i] < pivot_value:
            A[new_pivot_index], A[i] = A[i], A[new_pivot_index]
            new_pivot_index += 1
    # move pivot value to new_pivot_index
    A[new_pivot_index], A[right] = A[right], A[new_pivot_index]
    return new_pivot_index

def quicksort(A, lo, hi):
    print('quicksort: A={},lo={},hi={}'.format(A,lo,hi))
    if lo >= hi:
        # base case 0 or 1 element array is sorted by definition
        print('quicksort lo >= hi')
        return
    else: # lo < hi:
        print('quicksort partition')
        pivot_index = partition(A, lo, hi)
        print('quicksort quicksort lo={} to pivot_index={}'.format(lo, pivot_index))
        quicksort(A, lo, pivot_index)
        print('quicksort quicksort pivot_index+1={} to hi={}'.format(pivot_index+1, hi))
        quicksort(A, pivot_index+1, hi)

def qsort(A):
    print('A=', A)
    quicksort(A, 0, len(A) - 1)


def stable_sort_list(L):
    # TODO - you fill in here.
    return None


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
#                                        stable_sort_list))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       qsort))
