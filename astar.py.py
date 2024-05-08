def astar_search(start, goal, graph):
    """
    Performs the A* search algorithm to find the shortest path between a start and goal node in a graph.

    Args:
        start: The starting node.
        goal: The goal node.
        graph: The graph representing the game map.

    Returns:
        list: The shortest path from the start node to the goal node.
    """
    open_set = [(0, start)]
    closed_set = set()
    g_cost = {start: 0}
    f_cost = {start: heuristic(start, goal)}
    parent = {start: None}

    while open_set:
        _, current = min(open_set)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_set.remove((f_cost[current], current))
        closed_set.add(current)

        for neighbor, weight in graph[current].items():
            if neighbor in closed_set:
                continue

            new_g_cost = g_cost[current] + weight
            new_f_cost = new_g_cost + heuristic(neighbor, goal)

            if neighbor not in [n[1] for n in open_set] or new_f_cost < f_cost[neighbor]:
                open_set.append((new_f_cost, neighbor))
                g_cost[neighbor] = new_g_cost
                f_cost[neighbor] = new_f_cost
                parent[neighbor] = current

    return None

def heuristic(a, b):
    """
    Calculates the Euclidean distance between two nodes.

    Args:
        a: The first node.
        b: The second node.

    Returns:
        float: The Euclidean distance between the two nodes.
    """
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5