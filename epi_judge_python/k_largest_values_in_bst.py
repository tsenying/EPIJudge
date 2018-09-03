from test_framework import generic_test, test_utils


def x_find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    def inorder_traversal(tree):
        if tree.left:
            inorder_traversal(tree.left)
        T.append(tree.data)
        if tree.right:
            inorder_traversal(tree.right)
            #
    T = []
    inorder_traversal(tree)
    return T[-k:]

def find_k_largest_in_bst(tree, k):
    def find_k_largest_in_bst_helper(tree):
        if tree and (len(kth_largest_elements) < k):
            find_k_largest_in_bst_helper(tree.right)
            if (len(kth_largest_elements) < k):
                kth_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)
                #
    kth_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return kth_largest_elements

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
