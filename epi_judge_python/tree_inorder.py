from test_framework import generic_test
from bst_node import BstNode

left_left = BstNode(4)
left_right = BstNode(5)
left = BstNode(1, left_left, left_right)
right = BstNode(3)
root = BstNode(2,left,right)
print('root={}, left={}, right={}'.format(root,left,right))

def tree_traversal(tree, order, result):
    # TODO - you fill in here.
    # print('tree_traversal,tree={},result={},order={}'.format(tree, result, order))
    if tree:
        if order == -1:
            # print('Preorder: {}'.format(tree.data))
            result.append(tree.data)
        tree_traversal(tree.left, order, result)
        if order == 0:
            # print('Inorder: {}'.format(tree.data))
            result.append(tree.data)
        tree_traversal(tree.right, order, result)
        if order == 1:
            # print('Postorder: {}'.format(tree.data))
            result.append(tree.data)
    # print('result={}'.format(result))
    return result

def preorder_traversal(tree):
    result=[]
    return tree_traversal(tree, -1, result)

def inorder_traversal(tree):
    print('inorder_traversal')
    result=[]
    return tree_traversal(tree, 0, result)

def postorder_traversal(tree):
    result=[]
    return tree_traversal(tree, 1, result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
