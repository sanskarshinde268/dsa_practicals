from collections import deque

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
queue = deque([start])
parent = {start: None}
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    r, c = queue.popleft()
    if (r, c) == goal:
        break
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        nxt = (nr, nc)
        if (0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0
                and nxt not in parent):
            parent[nxt] = (r, c)
            queue.append(nxt)

if goal not in parent:
    print("No path exists.")
else:
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print("Shortest path (row, column):", path)
    print("Number of moves:", len(path) - 1)
