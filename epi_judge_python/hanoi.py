import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

def compute_tower_hanoi(num_rings):
    # 1. move n-1 pegs to aux pole
    # 2. move n-th disk to target
    # 3. move n-1 pegs onto target
    def move_pegs(n, source, target, aux):
        print('n={},source={},target={},aux={}'.format(n, source, target, aux))
        if n > 0:
            # 1. note aux and target poles switched in call
            move_pegs(n-1, source, aux, target)
            # 2.
            pegs[target].append(pegs[source].pop())
            result.append([source, target])
            # 3.
            move_pegs(n-1, aux, target, source)
    #
    result = []
    # initialize pegs
    pegs = [list(reversed(range(1, num_rings + 1)))] + \
            [[] for _ in range(1, NUM_PEGS)]
    # TODO - you fill in here.
    print('compute_tower_hanoi, pegs=', pegs)
    move_pegs(num_rings, 0, 1, 2)
    print('compute_tower_hanoi, pegs=', pegs)
    return result


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure("Illegal move from {} to {}".format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
