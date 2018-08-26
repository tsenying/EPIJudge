import functools
import math

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# input data format per line
# array(tuple(float[x], float[y], float[z]))	int[k]	array(float[distance])
# array of point coords, k, array of k closest starts distances
# e.g.
# [[3534.390007572918, -5506.091045838018, 6791.695314704164], [455.9867689353305, 210.16179816156728, 2534.6592773723114], [-8612.961122824476, 4822.423722433936, -9005.588371941652], [3230.9094454553924, -4549.215406723355, -8508.068323546328], [710.3634358674426, -8106.759457607544, 8375.017818259006]]	5	[2583.9097444028716, 9430.592588934343, 10174.544867444167, 11677.54634204817, 13361.867077127738]
class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        #
    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
        #
    def __lt__(self, rhs):
        return self.distance < rhs.distance
        #
    def __repr__(self):
        return str(self.distance)
        #
    def __str__(self):
        return self.__repr__()
        #
    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)

import heapq
def find_closest_k_stars(stars, k):
    # TODO - you fill in here.
    # maintain a k element max heap
    # 1. initialize max heap from first k elements
    # 2. for each star in stars:
    #      push next star distance
    #      pop max distance star
    # 3. resulting heap is kth closest stars
    print('k={}, stars={}'.format(k, stars))
    # max_heap = [-s.distance for s in stars[:k]]
    max_heap = []
    for _ in range(k):
        star = next(stars, None)
        print('star=',star)
        if star:
            heapq.heappush(max_heap, (-star.distance, star))
    print('1 max_heap=', max_heap)
    for star in stars:
        print('star type=', type(star), ',value=', star)
        heapq.heappushpop(max_heap, (-star.distance, star))
    print('end max_heap=', max_heap)
    return [star[1] for star in max_heap]


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(
        functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("k_closest_stars.py",
                                       "k_closest_stars.tsv",
                                       find_closest_k_stars_wrapper, comp))
