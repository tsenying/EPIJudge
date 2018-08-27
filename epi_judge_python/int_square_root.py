from test_framework import generic_test


def square_root(k):
    # TODO - you fill in here.
    left, right = 0, k
    while left <= right:
        mid = (right - left) // 2 + left
        mid_square = mid ** 2
        if mid_square < k:
            left = mid + 1
        elif mid_square == k:
            return mid
        else:
            right = mid - 1
    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
