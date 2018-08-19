import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

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

# make cycled list
l = build_linked_list([1,2,3,4,5])
start = l.next.next
end = start.next.next
end.next = start

def has_cycle(head):
    def cycle_len(end):
        start, count = end, 0
        while True:
            count += 1
            start = start.next
            if start is end:
                return count
    #
    #
    # TODO - you fill in here.
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            print ("has cycle")
            c_len = cycle_len(slow)
            print ("cycle length = {}".format(c_len))
            # start at beginning with two pointers offset by c_len
            ptr_ahead = head
            for _ in range(c_len):
                ptr_ahead = ptr_ahead.next
            ptr = head
            while ptr is not ptr_ahead:
                ptr, ptr_ahead = ptr.next, ptr_ahead.next
            return ptr
    print("NO cycle")
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", 'is_list_cyclic.tsv', has_cycle_wrapper))
