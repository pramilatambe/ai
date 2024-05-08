import sys
import heapq

def prim(graph):
    # Initialize the minimum spanning tree
    mst = []

    # Initialize the set of visited vertices
    visited = set()

    # Initialize the priority queue with the first vertex
    pq = [(0, 0)]  # (weight, vertex)

    while pq:
        # Extract the vertex with the minimum weight from the priority queue
        weight, vertex = heapq.heappop(pq)

        # If the vertex has already been visited, skip it
        if vertex in visited:
            continue

        # Mark the vertex as visited
        visited.add(vertex)

        # Add the edge to the minimum spanning tree
        mst.append((weight, vertex))

        # Add the adjacent vertices to the priority queue
        for neighbor, edge_weight in graph[vertex].items():
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor))

    return mst

# Example usage
graph = {
    0: {1: 2, 3: 6},
    1: {0: 2, 2: 3, 3: 8, 4: 5},
    2: {1: 3, 4: 7},
    3: {0: 6, 1: 8, 4: 9},
    4: {1: 5, 2: 7, 3: 9}
}


mst = prim(graph)
print("Minimum Spanning Tree:", mst)