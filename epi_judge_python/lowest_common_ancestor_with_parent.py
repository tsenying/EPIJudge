import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def x_lca(node0, node1):
    print('node0={}, node1={}'.format(node0, node1))
    # TODO - you fill in here.
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))
    print("depth0={}, depth1={}".format(depth0, depth1))
    # make depth0 the deeper node to simplify code
    if depth0 < depth1:
        depth0, depth1 = depth1, depth0
        node0, node1 = node1, node0

    # ascend deeper node to same depth as shallower node
    depth_diff = depth0 - depth1
    while depth_diff:
        depth_diff -= 1
        node0 = node0.parent

    # traverse up to root until nodes match
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0

def lca(node0, node1):
    # TODO - you fill in here.
    def node_depth(node):
        depth = -1
        while(node):
            depth += 1
            node = node.parent
        return depth
    # depths of each node
    depth0, depth1 = map(node_depth, [node0, node1])

    # for deeper node, traverse up until depth matches
    if (depth0 > depth1):
        diff = depth0 - depth1
        for _ in range(diff):
            node0 = node0.parent
    if (depth1 > depth0):
        diff = depth1 - depth0
        for _ in range(diff):
            node1 = node1.parent

    # travese up concurrently until LCA found
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
