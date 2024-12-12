def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])  # Path compression
    return parent[node]

def union(parent, rank, u, v):
    root_u = find_parent(parent, u)
    root_v = find_parent(parent, v)
    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    elif rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

def kruskal_mst(V, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = [i for i in range(V)]
    rank = [0] * V
    mst_weight = 0
    
    for u, v, weight in edges:
        if find_parent(parent, u) != find_parent(parent, v):
            mst_weight += weight
            union(parent, rank, u, v)
    
    return mst_weight

#example input
V = 3
edges = [(0, 1, 5), (1, 2, 3), (0, 2, 1)]

#personal input
#personal input
#adj = [[1, 2], [0, 3], [0, 4], [1], [2]]


print(kruskal_mst(V, edges))
