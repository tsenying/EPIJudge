from test_framework import generic_test


def is_symmetric(tree):
    # TODO - you fill in here.
    if tree is None:
        return True
        
    def check_symmetry(left, right):
        # base case: left is None and right is None
        if left is None and right is None:
            return True
        elif left and right:
            if left.data == right.data and \
                check_symmetry(left.left, right.right) and \
                check_symmetry(left.right, right.left):
                return True
        # one tree is empty, the other is not
        return False

    return check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
