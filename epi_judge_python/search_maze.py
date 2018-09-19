import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    # TODO - you fill in here.
    rows = len(maze)
    cols = len(maze[0])

    def adjacents(curr):
        # possible next steps
        neighbors = []
        left = Coordinate(curr.x-1, curr.y)
        right = Coordinate(curr.x+1, curr.y)
        top = Coordinate(curr.x, curr.y-1)
        bottom = Coordinate(curr.x, curr.y+1)

        if 0 <= left.x < rows and maze[left.x][left.y] == WHITE:
            neighbors.append(left)

        if 0 <= right.x < rows and maze[right.x][right.y] == WHITE:
            neighbors.append(right)

        if 0 <= top.y < cols and maze[top.x][top.y] == WHITE:
            neighbors.append(top)

        if 0 <= bottom.y < cols and maze[bottom.x][bottom.y] == WHITE:
            neighbors.append(bottom)

        print('---adjacents:curr={}, neighbors={}'.format(curr, neighbors))
        return neighbors

    def search_maze_dfs(curr, dest, visited=set()):
        if curr in visited:
            return False
        visited.add(curr)

        path.append(curr)
        print('-search_maze_dfs: curr={}, dest={}, path={}, visited={}'.format(curr, dest, path, visited))

        if curr == dest:
            return True
        for step in adjacents(curr):
            print('--search_maze_dfs step=', step)
            if search_maze_dfs(step, dest, visited):
                return True
        path.pop()
        return False

    print('start={}, end={}, maze dims={},{}, maze={}'.format(s, e, len(maze), len(maze[0]), maze))
    path = []
    search_maze_dfs(s, e)
    print('+++search_maze path=', path)
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            path_i_1 = path[i - 1]
            path_i = path[i]
            print('path_element_is_feasible path[i - 1]={}, path[i]={}'.format(path[i - 1], path[i]))
            print('maze(path[i - 1])={}, maze[path[i]]={}'.format(maze[path_i_1.x][path_i_1.y], maze[path_i.x][path_i.y]))
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
