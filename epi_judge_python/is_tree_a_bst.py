from test_framework import generic_test

# range check version,
# need initial range of negative to postive infinity for node value
def range_check_is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    if tree.data >= low_range and tree.data <= high_range:
        return (is_binary_tree_bst(tree.left, low_range, tree.data) and
                is_binary_tree_bst(tree.right, tree.data, high_range))
    else:
        return False

# use fact that for BST inorder traversal of nodes are in sorted order
def foo_is_binary_tree_bst(tree):
    def inorder_traversal(tree, previous_node_key=None):
        if tree:
            if tree.left:
                ordered = inorder_traversal(tree.left, previous_node_key)
                if not ordered:
                    return False

            if previous_node_key:
                if previous_node_key > tree.data:
                    ordered = False
                else:
                    ordered = True
            previous_node_key = tree.data

            if tree.right:
                ordered = inorder_traversal(tree.right, previous_node_key)
                if not ordered:
                    return False
        return ordered
    return inorder_traversal(tree)

# Solution from https://jeremykun.com/2012/09/16/trees-a-primer/
def inorder(root, f):
    ''' traverse the tree "root" in-order calling f on the
       associated node (i.e. f knows the name of the field to
       access). '''
    if not root:
        return
    if root.left != None:
      inorder(root.left, f)

    f(root)

    if root.right != None:
      inorder(root.right, f)

def is_binary_tree_bst(tree):
    numbers = []
    f = lambda node: numbers.append(node.data)

    inorder(tree, f)

    # print("\n---numbers=", numbers)
    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            # print("i=", i, "numbers[i-1]=", numbers[i-1], "numbers[i]", numbers[i])
            return False
    return True



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

def xis_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
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
