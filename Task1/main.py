import heapq

def dijkstra(graph, start):

    pq = []
    heapq.heappush(pq, (0, start))

    # Initialize distances to infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # Distance to the start node is 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If a shorter distance has already been found, skip this node
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
'''def DFS(graph, start, visited_node, min_path):
    visited_node.add(start)  # Use 'start' consistently
    min_path.append(start)

    # Check if the current node is one of the target nodes
    if start == 7 or start == 5 or start == 6:
        return min_path

    # Explore all neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited_node:  # Check if the neighbor is unvisited
            result = DFS(graph, neighbor, visited_node, min_path)
            if result:  # If a valid path is found, return it
                return result

    min_path.pop()  # Backtrack
    return None  # Return None if no path found
'''
# Your graph input
graph = {
    0: [(1, 2), (7, 3), (3, 2)],
    1: [(0, 1), (4, 4)],
    3: [(0, 1), (5, 7)],
    4: [(6, 4)],
    5: [(6, 2)],
    6: [],
    7: [(4, 5), (5, 6)]
}

start_node = 0
#visited = set()
#path=[]
distances = dijkstra(graph, start_node)
#dfs_distance = DFS(graph, start_node,visited,path)

print(f"Shortest path to node 7: {distances[7]}")
print(f"Shortest path to node 5: {distances[5]}")
print(f"Shortest path to node 6: {distances[6]}")
