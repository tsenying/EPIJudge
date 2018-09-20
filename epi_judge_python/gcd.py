from test_framework import generic_test

# chapter 15 intro greatest common divisor
# using Euclidean algorithm: https://en.wikipedia.org/wiki/Euclidean_algorithm
def gcd(x, y):
    # TODO - you fill in here.
    print('x={}, y={}, x%y={}'.format(x, y, (x%y if y!=0 else -1)))
    if y == 0:
        return x
    else:
        # after modulo, result will be less than y, so switch order
        # if y > x, then x%y is x, so next recursive call flips order and
        # it's as if initially called with gcd(y,x), just one extra call, i.e.
        # gcd(3,14) == gcd(14,3)
        return gcd(y, x%y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
