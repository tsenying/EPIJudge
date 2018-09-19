import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A):
    # TODO - you fill in here.
    # create list of endpoints decorated with start and end attributes
    # sort by time and start/end attribute
    #  if time is same:
    #   if start/end attribute different:
    #    start time comes first
    #   else:
    #    either order
    E = [p for event in A for p in [Endpoint(event.start, True), Endpoint(event.finish, False)]]
    # sort by time and start before end
    E.sort(key=lambda e: (e.time, not e.is_start)) # "not e.is_start so True (becomes 0) before False (becomes 1)"
    #
    count = 0
    max = 0
    for e in E:
        if e.is_start:
            count += 1
            if count > max:
                max = count
        else:
            count -= 1
    return max


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
