from test_framework import generic_test
from bst_node import BstNode

left_left = BstNode(4)
left_right = BstNode(5)
left = BstNode(1, left_left, left_right)
right = BstNode(3)
root = BstNode(2,left,right)
print('root={}, left={}, right={}'.format(root,left,right))
root_parent_l = BstNode(6,root)
root_parent_l_parent_l = BstNode(7, root_parent_l)

result = []
def tree_traversal(tree, result, order):
    # TODO - you fill in here.
    if tree:
        if order == -1:
            print('Preorder: {}'.format(tree.data))
            result.append(tree.data)
        tree_traversal(tree.left, result, order)
        if order == 0:
            print('Inorder: {}'.format(tree.data))
            result.append(tree.data)
        tree_traversal(tree.right, result, order)
        if order == 1:
            print('Postorder: {}'.format(tree.data))
            result.append(tree.data)
    print('tree={}, result={}'.format(tree, result))
    return result

def preorder_traversal(tree, result):
    result = tree_traversal(tree, result, -1)

def inorder_traversal(tree, result):
    result = tree_traversal(tree, result, 0)

def postorder_traversal(tree, result):
    result = tree_traversal(tree, result, 1)

def x_is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    def check_balance(tree):
        if tree:
            l_height = check_balance(tree.left)
            r_height = check_balance(tree.right)
            if (abs(l_height - r_height) > 1):
                raise RuntimeError('not balanced, node={}', tree)
            else:
                height = max(l_height, r_height) + 1
        else:
            height = -1
        # print('check_balance: height=', height)
        return height
    #
    balanced = True
    try:
        check_balance(tree)
    except RuntimeError as error:
        print(error)
        balanced = False
    #
    return balanced

import collections
def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )

    def check_balance(tree):
        # 1. base case, tree == None
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        #
        # Postorder traversal,
        #   check left sub tree, check right sub tree, check root
        left_result = check_balance(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balance(tree.right)
        if not right_result.balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1

        return BalancedStatusWithHeight(is_balanced, height)

    return check_balance(tree).balanced



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
