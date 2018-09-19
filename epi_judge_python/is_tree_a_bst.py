from test_framework import generic_test


def wrong_is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # TODO - you fill in here.
    print(type(tree))
    print(tree)
    if not tree:
        return True
    if tree.left:
        if tree.data >= tree.left.data:
            is_left_bst = is_binary_tree_bst(tree.left)
        else:
            is_left_bst = False
    else:
        is_left_bst = True
    if tree.right:
        if tree.data <= tree.right.data:
            is_right_bst = is_binary_tree_bst(tree.right)
        else:
            is_right_bst = False
    else:
        is_right_bst = True
    return (is_left_bst and is_right_bst)

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and
            is_binary_tree_bst(tree.right, tree.data, high_range))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
