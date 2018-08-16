from test_framework import generic_test
from test_framework.test_failure import TestFailure

def int_to_string(x):
    # TODO - you fill in here.
    chs=[]
    negative = False
    if x < 0:
        negative = True
        x = abs(x)
    while True:
        chs.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    if negative:
        chs.append('-')
    chs.reverse()
    return ''.join(chs)


INTS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def string_to_int(s):
    # TODO - you fill in here.
    n = 0
    negative = False
    if s[0] == '-':
        negative = True
        s = s[1:]
    for i in range(len(s)):
        n = (n * 10) + INTS[s[i]]
    if negative:
        n = -n
    return n


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
