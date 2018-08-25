from test_framework import generic_test

from bst_node import BstNode
# preorder = [1,2,3], inorder=[2,1,3], ["1", "2", "3"]
# preorder = [1, 2, 3, 4]	inorder = [4, 3, 2, 1]	["1", "2", "null", "3", "null", "4"]

# preorder = ['H','B','F','E','A','C','D','G','I']
# inorder = ['F','B','A','E','H','C','D','I','G']
pl = ['B','F','E','A']
il = ['F','B','A','E']
pr = ['C','D','G','I']
ir = ['C','D','I','G']
# left subtree
a = BstNode('A')
e = BstNode('E', a)
f = BstNode('F')
b = BstNode('B',f,e)
# right subtree
i = BstNode('I')
g = BstNode('G',i)
d = BstNode('D',None,g)
c = BstNode('C',None,d)
h = BstNode('H',b,c)

def binary_tree_from_preorder_inorder(preorder, inorder):
    def reconstruct_tree(preorder, inorder):
        # TODO - you fill in here.
        # 1. root is first node in preorder traversal
        # 2. use root to divide inorder traversal into left and right subtrees (inorder)
        # 3. use (left,right) inorder traversal set to partition preorder traversal
        #    after root element into (left,right) preorder traversal
        #
        print('preorder={},inorder={}'.format(preorder,inorder))
        if not preorder:
            print("returning None")
            return None
        # 1.
        root_value = preorder[0]
        root = BstNode(root_value)
        # 2.
        root_index = inorder.index(root_value)
        # root_index = element_index[root_value]
        print('root_index=',root_index)
        # 3.
        inorder_left_tree = inorder[:root_index]
        inorder_right_tree = inorder[root_index+1:]
        print('inorder_left_tree={},inorder_right_tree={}'.format(inorder_left_tree,inorder_right_tree))
        preorder_left_tree = preorder[1:root_index+1]
        preorder_right_tree = preorder[root_index+1:]
        print('preorder_left_tree={},preorder_right_tree={}'.format(preorder_left_tree, preorder_right_tree))
        #
        root.left = reconstruct_tree(preorder_left_tree, inorder_left_tree)
        root.right = reconstruct_tree(preorder_right_tree, inorder_right_tree)
        print('root={}'.format(root))
        return root
    #
    # cache value to index map for inorder traversal to speed lookup
    # element_index = {data: i for i,data in enumerate(inorder)}
    return reconstruct_tree(preorder, inorder)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
