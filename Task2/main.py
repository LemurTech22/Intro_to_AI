import math


def aStarAlgo(start_node, end_node):
    openSet = set([start_node])  # creates a set of calculated nodes
    closedSet = set()  # creates a set of nodes evalulated
    g = {}
    parent = {}

    g[start_node] = 0  # distance of starting node from itself is zero
    parent[start_node] = start_node  # start is root node i.e it has no parent node.

    while len(openSet) > 0:
        neighbor = None  # intialize to zero and updates if it finds a neighbor.

        # node with lowest f() is found
        for v in openSet:
            if neighbor is None or g[v] + heuristic(v, end_node) < g[neighbor] + heuristic(neighbor,end_node):  # finding the cost function
                neighbor = v  # update with the next node.

        if neighbor == end_node:
            path = []
            cost = g[neighbor]
            while parent[neighbor] != neighbor:
                path.append(neighbor)
                neighbor = parent[neighbor]

            path.append(start_node)
            path.reverse()

            return path, cost

        if neighbor is None:
            print("Path doesnt exist ")
            return None, None

        for adj_node, weight in get_neighbors(neighbor):
            if adj_node not in openSet and adj_node not in closedSet:
                openSet.add(adj_node)

                parent[adj_node] = neighbor
                g[adj_node] = g[neighbor] + weight

            else:
                if g[adj_node] > g[neighbor] + weight:
                    g[adj_node] = g[neighbor] + weight
                    parent[adj_node] = neighbor

                    if adj_node in closedSet:
                        closedSet.remove(adj_node)
                        openSet.add(adj_node)

        openSet.remove(neighbor)
        closedSet.add(neighbor)

    print("Path doesn't exist")
    return None, None


def heuristic(n, goalNode):
    return math.sqrt((goalNode[0] - n[0]) ** 2 + (goalNode[1] - n[1]) ** 2)


def get_neighbors(node):
    if node in graph_node:
        return graph_node[node]
    else:
        return None


if __name__ == '__main__':
    global graph_node
    # change nodes and weights
    city_matrix = {
        (0, 0): [((0, 1), 4), ((1, 0), 7)],
        (0, 1): [((0, 2), 5), ((1, 1), 9)],
        (0, 2): [((1, 2), 8), ((0, 3), 3)],
        (0, 3): [((0, 4), 4), ((1, 3), 7)],
        (0, 4): [((1, 4), 6)],

        (1, 0): [((0, 0), 7), ((2, 0), 9), ((1, 1), 4)],
        (1, 1): [((1, 0), 4), ((2, 1), 6)],
        (1, 2): [((0, 2), 8), ((2, 2), 5)],
        (1, 3): [((0, 3), 7), ((2, 3), 9)],
        (1, 4): [((0, 4), 6), ((2, 4), 3)],

        (2, 0): [((1, 0), 9), ((3, 0), 5), ((2, 1), 4)],
        (2, 1): [((1, 1), 6), ((2, 2), 3), ((3, 1), 7)],
        (2, 2): [((1, 2), 5), ((2, 3), 2), ((3, 2), 8)],
        (2, 3): [((1, 3), 9), ((2, 4), 4), ((3, 3), 3)],
        (2, 4): [((1, 4), 3), ((3, 4), 6)],

        (3, 0): [((2, 0), 5), ((3, 1), 3), ((4, 0), 7)],
        (3, 1): [((2, 1), 7), ((3, 2), 2), ((4, 1), 4)],
        (3, 2): [((2, 2), 8), ((3, 3), 5), ((4, 2), 3)],
        (3, 3): [((2, 3), 3), ((3, 4), 4), ((4, 3), 2)],
        (3, 4): [((2, 4), 6), ((4, 4), 1)],

        (4, 0): [((3, 0), 7), ((4, 1), 5)],
        (4, 1): [((3, 1), 4), ((4, 2), 3)],
        (4, 2): [((3, 2), 3), ((4, 3), 2)],
        (4, 3): [((3, 3), 2), ((4, 4), 1)],
        (4, 4): [((3, 4), 1)]

    }
    graph_node = city_matrix
    start_node = (0, 0)
    goal_node = (4, 4)

    result, cost = aStarAlgo(start_node, goal_node)

    if result is not None:
        print(f"Path: {result}")
        print(f"The total Cost is: {cost}")
    else:
        print("Path doesn't exist")
    # change nodes and weights
    # creates a 5 x 5 city grid
    city_matrix = {
        (0, 0): [((0, 1), 6), ((1, 0), 11)],
        (0, 1): [((0, 2), 3), ((1, 1), 7)],
        (0, 2): [((1, 2), 10), ((0, 3), 4)],
        (0, 3): [((0, 4), 5), ((1, 3), 12)],
        (0, 4): [((1, 4), 9)],

        (1, 0): [((0, 0), 11), ((2, 0), 7), ((1, 1), 5)],
        (1, 1): [((1, 0), 5), ((2, 1), 4)],
        (1, 2): [((0, 2), 10), ((2, 2), 2)],
        (1, 3): [((0, 3), 12), ((2, 3), 6)],
        (1, 4): [((0, 4), 9), ((2, 4), 4)],

        (2, 0): [((1, 0), 7), ((3, 0), 4), ((2, 1), 6)],
        (2, 1): [((1, 1), 4), ((2, 2), 5), ((3, 1), 7)],
        (2, 2): [((1, 2), 2), ((2, 3), 6), ((3, 2), 4)],
        (2, 3): [((1, 3), 6), ((2, 4), 3), ((3, 3), 8)],
        (2, 4): [((1, 4), 4), ((3, 4), 2)],

        (3, 0): [((2, 0), 4), ((3, 1), 6), ((4, 0), 3)],
        (3, 1): [((2, 1), 7), ((3, 2), 5), ((4, 1), 3)],
        (3, 2): [((2, 2), 4), ((3, 3), 3), ((4, 2), 6)],
        (3, 3): [((2, 3), 8), ((3, 4), 2), ((4, 3), 5)],
        (3, 4): [((2, 4), 2), ((4, 4), 1)],

        (4, 0): [((3, 0), 3), ((4, 1), 4)],
        (4, 1): [((3, 1), 3), ((4, 2), 5)],
        (4, 2): [((3, 2), 6), ((4, 3), 3)],
        (4, 3): [((3, 3), 5), ((4, 4), 2)],
        (4, 4): [((3, 4), 1)]
    }

    graph_node = city_matrix
    result, cost = aStarAlgo(start_node, goal_node)

    if result is not None:
        print("\nUpdated Weights: ")
        print(f"Path: {result}")
        print(f"The total Cost is: {cost}")
    else:
        print("Path doesn't exist")