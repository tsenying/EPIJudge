from test_framework import generic_test

# chapter 16 dynamic programming

# recursive solution with exponential run time
def fibonacci_O_exp(n, cache={}):
    # TODO - you fill in here.
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

# O(n) time in O(1) space
def fibonacci(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
