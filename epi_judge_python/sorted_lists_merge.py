from test_framework import generic_test


def x_merge_two_sorted_lists(L1, L2):
    print('L1=',L1)
    print('L2=',L2)
    # TODO - you fill in here.
    R, R_end = None, None
    #
    # init merged list
    if L1 and L2:
        if L1.data <= L2.data:
            R, R_end = L1, L1
            L1 = L1.next
        else:
            R, R_end = L2, L2
            L2 = L2.next
            print("if L2: R=",R)
    elif L1:
        R, R_end = L1, L1
        L1 = L1.next
    elif L2:
        R, R_end = L2, L2
        L2 = L2.next
    #
    loop = 0
    while L1 and L2:
        if L1.data <= L2.data:
            R_end.next = L1
            R_end = L1
            L1 = L1.next
            while loop < 1:
                loop +=1
        else:
            R_end.next = L2
            R_end = L2
            L2 = L2.next
    while L1:
        R_end.next = L1
        R_end = L1
        L1 = L1.next
    while L2:
        R_end.next = L2
        R_end = L2
        L2 = L2.next
    # R_end.next = None
    print('R=', R)
    return R

class ListNode(object):
    """docstring for ."""
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def merge_two_sorted_lists(L1, L2):
    head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    tail.next = L1 or L2
    return head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
