import heapq
def astar(start,goal,grid):
    rows=len(grid)
    cols=len(grid[0])
    def neighbors(node):
        x,y=node
        all_neighbors=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        valid_neighbor=[(nx,ny)for nx,ny in all_neighbors if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0]
        return valid_neighbor

    def heuristic(node,goal):
        x1,y1=node
        x2,y2=goal
        return abs(x1-x2)+abs(y1-y2)

    open_set=[(0,start)]
    came_from={}
    g_score={start:0}

    while open_set:
        current_cost,current_node=heapq.heappop(open_set)
        if current_node==goal:
            path=[]
            while current_node in came_from:
                path.append(current_node)
                current_node=came_from[current_node]
            return path[::-1]

        for neighbor in neighbors(current_node):
            tentative_g_score=g_score[current_node] + 1
            if neighbor not in g_score or tentative_g_score<g_score[neighbor]:
                came_from[neighbor]=current_node
                g_score[neighbor]=tentative_g_score
                f_score=tentative_g_score+heuristic(neighbor,goal)
                heapq.heappush(open_set,(f_score,neighbor))

    return None


def get_matrix_input():
    rows=int(input("entr no of row"))
    cols=int(input("entr no of cols"))
    print("enter the ellement of metrix 0 for empty one for obstacle")
    grid=[]
    for _ in range(rows):
        row=list(map(int,input().split()))
        grid.append(row)
    return grid

start_x=int(input("enter the start x"))
start_y=int(input("enter start y"))
start=(start_x,start_y)

goal_x=int(input("enter the goal x"))
goal_y=int(input("enter the goal y"))
goal=(goal_x,goal_y)

grid=get_matrix_input()
grid[1][3]=1

path=astar(start,goal,grid)
if path:
    print("path found",path)
else:
    print("not found")

#input=Enter start position x-coordinate: 0
Enter start position y-coordinate: 0
Enter goal position x-coordinate: 2
Enter goal position y-coordinate: 3
Enter the number of rows: 3
Enter the number of columns: 4
Enter the elements of the matrix (0 for empty cell, 1 for obstacle):
0 0 0 0
0 1 1 0
0 0 0 0