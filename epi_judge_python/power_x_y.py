from test_framework import generic_test


def power(x, y):
    # TODO - you fill in here.
    result, exp = 1.0, y

    if y < 0:
        exp, x = -exp, 1.0/x

    if exp:
        if exp & 1:
            result = x * power(x, exp&(exp-1)) # x&(x-1) clears lowest set bit
        else:
            half = power(x, exp >> 1) # x >> 1 divides by half
            result = half * half
    return result

# def power(x, y):
#     result, power = 1.0, y
#     if y < 0:
#         power, x = -power, 1.0 / x
#     while power:
#         if power & 1:
#             result *= x
#             print("LSB is 1, power=", bin(power), ", result=", result)
#         print("1. x=", x, "power=", power)
#         x, power = x * x, power >> 1
#         print("2. x=", x, "power=", power)
#     return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
