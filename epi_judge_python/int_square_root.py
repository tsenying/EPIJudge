from test_framework import generic_test


def x_square_root(k):
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

# Given a non-negative integer
# find the largest number whose square is less than the input number
def square_root(k):
    # find by bisection
    # halve the number and get square
    # if square == number, return largest
    # if midpoint**2 < number
    #   record as largest
    #   midpoint = L + (U - M) // 2
    # elif midpoint**2 > number
    #   midpoint = L + (M - L) // 2
    L, U = 0, k
    while L <= U:
        mid = L + (U - L) // 2
        mid_square = mid ** 2
        if mid_square <= k:
            # look to higher side
            L = mid + 1
        else:
            # mid_square > k, look to lower side
            U = mid - 1
    return U



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
