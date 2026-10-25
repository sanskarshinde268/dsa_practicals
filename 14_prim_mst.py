# Prim's Minimum Spanning Tree using an adjacency matrix.
INF = float("inf")
vertices = ["Gate", "Library", "Canteen", "Lab", "Hostel"]
# 0 means no direct edge; graph is undirected.
graph = [
    [0,   4,   2,   0,   0],
    [4,   0,   1,   5,   0],
    [2,   1,   0,   8,  10],
    [0,   5,   8,   0,   2],
    [0,   0,  10,   2,   0]
]
n = len(vertices)
key = [INF] * n
parent = [-1] * n
in_mst = [False] * n
key[0] = 0

for _ in range(n):
    u = -1
    for i in range(n):
        if not in_mst[i] and (u == -1 or key[i] < key[u]):
            u = i
    if u == -1 or key[u] == INF:
        break
    in_mst[u] = True
    for v in range(n):
        weight = graph[u][v]
        if weight != 0 and not in_mst[v] and weight < key[v]:
            key[v] = weight
            parent[v] = u

total = 0
print("Prim MST edges:")
for v in range(1, n):
    if parent[v] != -1:
        w = graph[v][parent[v]]
        print(f"{vertices[parent[v]]} -- {vertices[v]}: {w}")
        total += w
print("Total weight:", total)
if sum(in_mst) != n:
    print("Warning: graph is disconnected; not all vertices are connected.")
