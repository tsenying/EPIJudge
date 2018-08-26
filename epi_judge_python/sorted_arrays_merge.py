from test_framework import generic_test

# examples: sorted_arrays, merged array
# 1. [[-1, 0], [-2]]	[-2, -1, 0]
# 2. [[-2, 0, 4, 5, 6], [1], [-1], [-5, 3, 3, 3, 4], [-3, -1, 4], [-6, 0, 3, 3]]	[-6, -5, -3, -2, -1, -1, 0, 0, 1, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6]

import heapq
# sorted_arrays is an array of sorted arrays
def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    print('sorted_arrays=', sorted_arrays)
    sorted = []
    # construct initial heap with first element from each sorted array
    min_heap = [(array[0],i) for i, array in enumerate(sorted_arrays) if array]
    heapq.heapify(min_heap)
    print('min_heap=', min_heap)
    #
    # pop min and append to sorted
    # maintain ptrs into arrays so don't need to
    ptrs = [1] * len(sorted_arrays)
    empty = 0
    num_arrays = len(sorted_arrays)
    while empty < num_arrays:
        # print('empty=', empty)
        min_tuple = heapq.heappop(min_heap)
        # print('min_tuple=', min_tuple)
        sorted.append(min_tuple[0])
        # print('sorted=', sorted, ', min_heap=', min_heap, ',sorted_arrays=', sorted_arrays)
        #
        # push another element from array where last min came from onto heap
        try:
            # next = sorted_arrays[min_tuple[1]].pop(0)
            next = sorted_arrays[min_tuple[1]][ptrs[min_tuple[1]]]
            ptrs[min_tuple[1]] += 1
            heapq.heappush(min_heap, (next, min_tuple[1]))
        except IndexError:
            # print("sorted_arrays {} array empty".format(min_tuple[1]))
            empty += 1
    return sorted


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
