from test_framework import generic_test
from bst_node import BstNode

left_left = BstNode(4)
left_right = BstNode(5)
left = BstNode(1, left_left, left_right)
right = BstNode(3)
root = BstNode(2,left,right)
print('root={}, left={}, right={}'.format(root,left,right))

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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
