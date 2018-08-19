from test_framework import generic_test


import list_node
def build_linked_list(data):
    """A helper function for linked list parser.

    Constructs a linked list from a list of values.

    :param data - list of values.
    """
    head = None
    for x in reversed(data):
        head = list_node.ListNode(x, head)
    return head

def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    dummy_head = sublist_head = list_node.ListNode(0, L)
    # traverse to beginning of sublist
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # traverse and reverse sublist
    sublist_iter = sublist_head.next # current end of traversed list
    for _ in range(finish - start):
        temp = sublist_iter.next # this one flips to front
        sublist_iter.next, temp.next, sublist_head.next = \
            (temp.next, # becomes last node in traversed sublist
             sublist_head.next, # point to current beginning
             temp # end now becomes front
             )

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
