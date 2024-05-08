# Graph Coloring Problem using Backtracking Algorithm

# Function to check if a color can be assigned to a vertex
def is_safe(graph, color, v, c, n):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

# Function to solve the graph coloring problem using backtracking
def graph_coloring(graph, m, n):
    color = [-1] * n

    # Function to backtrack and find a solution
    def backtrack(v):
        if v == n:
            print_solution(color)
            return True

        for c in range(m):
            if is_safe(graph, color, v, c, n):
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = -1

        return False
    
    backtrack(0)

# Function to print the solution
def print_solution(color):
    print("Solution found:")
    for c in color:
        print(c, end=" ")
    print()

# Example usage
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
graph_coloring(graph, 3, 4)