# https://jeremykun.com/2013/01/22/depth-and-breadth-first-search

class Node:
    """docstring for Node."""
    def __init__(self, value):
        self.value = value
        self.adjacentNodes = []
        #
    def __repr__(self):
        return ('Node value={}, adjacentNodes={}'.format(self.value, self.adjacentNodes))

nodes_set = ['A','B','C','D','E','F']

adjacency_list = {
    'A': {'B'},
    'B': {'C'},
    'C': {'E'},
    'D': {'B'},
    'E': {'D','F'},
}

# build base nodes
nodes = {}
for n in nodes_set:
    node = Node(n)
    nodes[n] = node

# populate the node adjacency list
for key, edge_list in adjacency_list.items():
    print(key, edge_list)
    node = nodes[key]
    print('node before add edges', node)
    for end_node in edge_list:
        node.adjacentNodes.append(nodes[end_node])
        print('node after add edges', node)

def depthFirstSearch(node, searchValue, visitedNodes=set()):
    if node.value == searchValue:
        # match found
        return True
        #
    # prevent looping through visisted nodes
    visitedNodes.add(node)
    for adjacent_node in node.adjacentNodes:
        if adjacent_node not in visitedNodes:
            if depthFirstSearch(adjacent_node, searchValue, visitedNodes):
                return True
    #
    return False

# non-recursive version, using stack
def depthFirst(node, searchValue):
    visitedNodes = set()
    # stack maintains nodes to be visited
    # initialize stack with first node
    stack = [node]
    #
    while len(stack) > 0:
        node = stack.pop()
        if node in visitedNodes:
            continue
        #
        if node.value == searchValue:
            return True
        visitedNodes.add(node)
        # depth first search of adjacent nodes
        # for adjNode in node.adjacentNodes:
        #     if adjNode not in visitedNodes:
        #         stack.append(adjNode)
        stack.extend([adjNode for adjNode in node.adjacentNodes if adjNode not in visitedNodes])
        #
    return False

from collections import deque
def breadthFirst(node, searchValue):
    visitedNodes = set()
    # queue maintains nodes to be visited in breadth first search order
    # difference with depth first is that queue used instead of stack
    # initialize stack with first node
    queue = deque([node])
    #
    while len(queue) > 0:
        node = queue.popleft()
        if node in visitedNodes:
            continue
        #
        if node.value == searchValue:
            return True
        visitedNodes.add(node)
        # depth first search of adjacent nodes
        for adjNode in node.adjacentNodes:
            if adjNode not in visitedNodes:
                queue.append(adjNode)
        #
    return False
