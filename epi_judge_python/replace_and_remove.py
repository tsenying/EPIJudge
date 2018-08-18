import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# s=['a','b','b','a'] => ['d', 'd', 'd', 'd']
# s=['a','b','b','a','c'] => ['d', 'd', 'd', 'd', 'c']

def replace_and_remove(size, s):
    # TODO - you fill in here.
    # 1. remove 'b's
    # 2. replace 'a' with 'dd'
    write_index = 0
    a_count, b_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        else:
            b_count += 1
        if s[i] == 'a':
            a_count += 1
    print ('s={},\na_count={}'.format(s,a_count))
    #
    reduced_count = size - b_count
    current_index = reduced_count - 1
    final_count = reduced_count + a_count
    write_index = final_count - 1
    print('reduced_count={},current_index={},final_count={},write_index={}'.format(reduced_count,current_index,final_count,write_index))
    #
    for i in range(reduced_count):
        if s[current_index] != 'a':
            # move non 'a' to end
            s[write_index] = s[current_index]
            write_index -= 1
        else:
            # replace 'a' with 'dd'
            s[write_index-1], s[write_index] = 'd', 'd'
            write_index -= 2
        current_index -= 1
    return final_count


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
