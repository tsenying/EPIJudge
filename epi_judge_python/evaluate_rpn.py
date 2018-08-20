from test_framework import generic_test

# Rules of RPN
# 1. [-](\d+)
# 2. "A,B,o": where A,B are RPN and o = [+-x/]
# e.g. "3,4,+,2,x,1,+"

class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

# Hint: process subexpressions, keeping values on a stack
#       How should operators be handles?
import re, operator
def evaluate(expression):
    print('\n----- evaluate expression=', expression)
    # TODO - you fill in here.
    def operate(A, B, o):
        if o == '+':
            return operator.add(A,B)
        elif o == '-':
            return operator.sub(A,B)
        elif o == '*':
            return operator.mul(A,B)
        elif o == '/':
            return operator.floordiv(A,B)
    #
    stack = []
    A, B, o = (None,)*3
    re_digits = r'-*\d+'
    re_operand = r'^[+-/*]+'
    for t in expression.split(','):
        print("t=",t)
        m = re.match(re_digits, t)
        if m:
            print('digits: m=', m)
            digits = int(m.group())
            stack.append(digits)
            print('digits: stack=', stack)
            continue
        #
        m = re.match(re_operand, t)
        if m:
            print('operand: m=', m)
            o = m.group()
            B = stack.pop()
            A = stack.pop()
            result = operate(A, B, o)
            stack.append(result)
            print('operand: stack=', stack)
            continue
        raise InputError(t, 'Unknown token')
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
