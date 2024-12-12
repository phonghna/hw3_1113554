def dfs_traversal(adj):
    def dfs(node):
        visited[node] = True
        traversal.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    V = len(adj)
    visited = [False] * V
    traversal = []
    dfs(0)
    return traversal

#example input
adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]


#personal input
#adj = [[1, 2], [0, 3], [0, 4], [1], [2]]



print(dfs_traversal(adj))