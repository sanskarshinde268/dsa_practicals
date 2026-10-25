import heapq

# 0 = free cell, 1 = obstacle
maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
rows, cols = len(maze), len(maze[0])

def heuristic(cell):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

open_heap = [(heuristic(start), 0, start)]
came_from = {start: None}
g_score = {start: 0}
closed = set()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while open_heap:
    f, g, current = heapq.heappop(open_heap)
    if current in closed:
        continue
    if current == goal:
        break
    closed.add(current)

    r, c = current
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        neighbor = (nr, nc)
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue
        if maze[nr][nc] == 1 or neighbor in closed:
            continue
        tentative_g = g_score[current] + 1
        if tentative_g < g_score.get(neighbor, float("inf")):
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g
            heapq.heappush(open_heap,
                           (tentative_g + heuristic(neighbor), tentative_g, neighbor))

if goal not in came_from:
    print("No path exists.")
else:
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    print("A* path (row, column):", path)
    print("Number of moves:", len(path) - 1)
