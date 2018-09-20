# exponential function
# Recursion: chapter 15
# Dynamic programming chapter 16

# Function to calculate exponential of base x to the power of exponent y
# Only deal with integer exponents
# handle negative exponents
def exp(base, exponent):
    negative = False
    if exponent == 0:
        return 1
    if exponent < 0:
        negative = True
        exponent = -exponent
    result = base
    for _ in range(1, exponent):
        result *= base
    if negative:
        result = 1/result
    return result

def test_exp_zero():
    assert exp(2, 0) == 1
    assert exp(9, 0) == 1

def test_exp_postive():
    assert exp(2, 1) == 2
    assert exp(2, 8) == 256

def test_exp_negative():
    assert exp(2, -3) == 1/8
    assert exp(2, -1) == 1/2
