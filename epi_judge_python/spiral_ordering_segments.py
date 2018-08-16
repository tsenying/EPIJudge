from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    def layer_clockwise(offset):
        if offset == (len(square_matrix) - offset -1):
            # square_matrix has off dimension, offset is at center of matrix
            spiral_order.append(square_matrix[offset][offset])
            return
        #
        spiral_order.extend(square_matrix[offset][offset: -1 - offset])
        spiral_order.extend(list(zip(*square_matrix))[-1 - offset][offset: -1 - offset])
        spiral_order.extend(square_matrix[-1 - offset][-1 - offset:offset:-1])
        spiral_order.extend(list(zip(*square_matrix))[offset][-1-offset:offset:-1])
    #
    spiral_order = []
    for offset in range((len(square_matrix) + 1) // 2):
        layer_clockwise(offset)
    return spiral_order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
