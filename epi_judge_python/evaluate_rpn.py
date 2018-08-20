from test_framework import generic_test

# Rules of RPN
# 1. [-](\d+)
# 2. "A,B,o": where A,B are RPN and o = [+-x/]
# e.g. "3,4,+,2,x,1,+"

# Hint: process subexpressions, keeping values on a stack
#       How should operators be handles?
import re, operator
def evaluate(expression):
    # TODO - you fill in here.
    def operate(A, B, o):
        if o == '+':
            return operator.add(A,B)
        elif o == '-':
            return operator.subtract(A,B)
        elif o == 'x':
            return operator.mul(A,B)
        elif o == '/':
            return operator.floordiv(A,B)
    #
    stack = []
    A, B, o = (None,)*3
    re_digits = r'-*\d+'
    re_operand = r'^[+-x/]+'
    for t in expression.split(','):
        print("t=",t)
        if not A:
            m = re.match(re_digits, t)
            print('if not A: m=', m)
            A = int(m.group())
            stack.append(A)
            print('if not A: stack=', stack)
        elif not B:
            m = re.match(re_digits, t)
            print('if not B: m=', m)
            B = int(m.group())
            stack.append(B)
            print('if not B: stack=', stack)
        elif not o:
            m = re.match(re_operand, t)
            print('if not o: m=', m)
            o = m.group()
            B = stack.pop()
            A = stack.pop()
            result = operate(A, B, o)
            stack.append(result)
            print('if not o: stack=', stack)
            A, o = (None,)*2
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
