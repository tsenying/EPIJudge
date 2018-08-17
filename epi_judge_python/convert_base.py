from test_framework import generic_test

DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
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

def string_to_decimal(num_as_string, base):
    decimal = 0
    is_negative = False
    if num_as_string[0] == '-':
        is_negative = True
        num_as_string = num_as_string[1:]
    for i in range(len(num_as_string)):
        decimal = (decimal * base) + DIGITS[num_as_string[i]]
    if is_negative:
        decimal = -decimal
    return decimal

CHARS=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def decimal_to_base(x, base):
    chs=[]
    negative = False
    if x < 0:
        negative = True
        x = -x
    while True:
        chs.append(CHARS[x % base])
        x //= base
        if x == 0:
            break
    if negative:
        chs.append('-')
    chs.reverse()
    return ''.join(chs)

# Assume 2 <= b1,b2 <= 16
# representation A=10, B=11, C=12, D=13, E=14, F=15
# string '615' base b1 7 to base b2 13
def x_convert_base(num_as_string, b1, b2):
    # TODO - you fill in here.
    print('num_as_string={n}, b1={b1}, b2={b2}'.format(n=num_as_string, b1=b1, b2=b2))
    decimal = string_to_decimal(num_as_string, b1)
    print('decimal=', decimal)
    number = decimal_to_base(decimal, b2)
    print('number=', number)
    return number

import functools, string
def string_to_int(num_as_string, base):
    number = functools.reduce(
        lambda x, c: x * base + string.hexdigits.index(c.lower()),
        num_as_string,
        0
    )
    return number

def construct_from_base(num_as_int, base):
    if num_as_int == 0:
        return ''
    else:
        return (construct_from_base(num_as_int // base, base) +
            string.hexdigits[num_as_int % base].upper())

def convert_base(num_as_string, b1, b2):
    is_negative = num_as_string[0] == '-'
    number = string_to_int(num_as_string[is_negative:], b1)
    if number == 0:
        target = '0'
    else:
        target = construct_from_base(number, b2)
    if is_negative:
        target = '-' + target
    return target

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
