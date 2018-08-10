from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.
    if x >= 0:
        s = str(x)
        r = ''
    else:
        s = str(-x)
        r = '-'

    size = len(s)
    for i in range(size):
        r += s[size-1-i]
    return int(r)

def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    if x < 0:
        result = -result
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
