import heapq

class Graph:
    def _init_(self):
        self.graph = {}

    def add_edge(self, src, dest, weight):
        self.graph.setdefault(src, []).append((dest, weight))
        self.graph.setdefault(dest, []).append((src, weight))

def prim(graph):
    mst = []
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapq.heapify(edges)

    while edges:
        weight, src, dest = heapq.heappop(edges)
        if dest not in visited:
            visited.add(dest)
            mst.append((src, dest, weight))
            for neighbor, weight in graph[dest]:
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, dest, neighbor))

    return mst


def kruskal(graph):
    mst = []
    parent = {v: v for v in graph}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        parent[find(u)] = find(v)

    edges = [(weight, src, dest) for src, adj in graph.items() for dest, weight in adj]
    edges.sort()

    for weight, src, dest in edges:
        if find(src) != find(dest):
            mst.append((src, dest, weight))
            union(src, dest)

    return mst

def main():
    graph = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        src, dest, weight = input("Enter source vertex, destination vertex, and weight separated by space: ").split()
        graph.add_edge(src, dest, int(weight))

    algorithms = {1: prim, 2: kruskal}
    choice = int(input("Choose algorithm:\n1. Prim's Algorithm\n2. Kruskal's Algorithm\nEnter choice: "))
    if choice in algorithms:
        minimum_spanning_tree = algorithms[choice](graph.graph)
        print(f"Minimum Spanning Tree ({'Prim' if choice == 1 else 'Kruskal'}'s Algorithm):")
        for edge in minimum_spanning_tree:
            print(edge)
    else:
        print("Invalid choice.")

if _name_ == "_main_":
    main()



#input=Enter the number of edges: 6
Enter source vertex, destination vertex, and weight separated by space: A B 4
Enter source vertex, destination vertex, and weight separated by space: A C 2
Enter source vertex, destination vertex, and weight separated by space: B C 5
Enter source vertex, destination vertex, and weight separated by space: B D 10
Enter source vertex, destination vertex, and weight separated by space: C D 3
Enter source vertex, destination vertex, and weight separated by space: C E 7
Choose algorithm:
1. Prim's Algorithm
2. Kruskal's Algorithm
Enter choice: 1
Minimum Spanning Tree (Prim's Algorithm):
('A', 'C', 2)
('C', 'E', 7)
('A', 'B', 4)
('C', 'D', 3)