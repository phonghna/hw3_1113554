from collections import deque

def bfs_traversal(adj):
    V = len(adj)
    visited = [False] * V
    traversal = []
    queue = deque([0])
    visited[0] = True
    
    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                
    return traversal

# Example input
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

#personal input
#adj = [[1, 2], [0, 3], [0, 4], [1], [2]]



print(bfs_traversal(adj))
