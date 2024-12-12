def create_adjacency_list(V, edges):
    adj_list = [[] for _ in range(V)]
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    for neighbors in adj_list:
        neighbors.sort()
    
    return adj_list

# Example input
V = 5
edges = [[0, 1], [0, 4], [4, 1], [4, 3], [1, 3], [1, 2], [3, 2]]

#personal input
# V = 6
# edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]



adj_list = create_adjacency_list(V, edges)
print(adj_list)
