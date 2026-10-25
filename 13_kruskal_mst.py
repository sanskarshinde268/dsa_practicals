# Kruskal's Minimum Spanning Tree using an adjacency-list-style edge list.
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

# Example campus graph: (place1, place2, distance/weight)
vertices = ["Gate", "Library", "Canteen", "Lab", "Hostel"]
edges = [
    ("Gate", "Library", 4), ("Gate", "Canteen", 2),
    ("Library", "Canteen", 1), ("Library", "Lab", 5),
    ("Canteen", "Lab", 8), ("Canteen", "Hostel", 10),
    ("Lab", "Hostel", 2)
]
index = {name: i for i, name in enumerate(vertices)}
parent = list(range(len(vertices)))
rank = [0] * len(vertices)
mst, total = [], 0

for u, v, w in sorted(edges, key=lambda e: e[2]):
    if union(parent, rank, index[u], index[v]):
        mst.append((u, v, w))
        total += w

print("Kruskal MST edges:")
for u, v, w in mst:
    print(f"{u} -- {v}: {w}")
print("Total weight:", total)
if len(mst) != len(vertices) - 1:
    print("Warning: graph is disconnected; no spanning tree covers every vertex.")
