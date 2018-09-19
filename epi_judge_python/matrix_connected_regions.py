from test_framework import generic_test

import collections
def flip_color(x, y, image):
    # TODO - you fill in here.
    rows = len(image)
    cols = len(image[0])
    print('flip_color, x={}, y={}, rows={}, cols={}, image={} '.format(x, y, rows, cols, image))
    # track initial color of coord
    color = image[x][y]
    q = collections.deque([(x,y)])
    # flip color of current coord
    image[x][y] = 1 - image[x][y]

    # BFS flip color of neighbors
    while q:
        x, y = q.popleft()
        for next_x, next_y in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= next_x < rows and 0 <= next_y < cols and image[next_x][next_y] == color:
                # flip color
                image[next_x][next_y] = 1 - image[next_x][next_y]
                q.append((next_x, next_y))

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
