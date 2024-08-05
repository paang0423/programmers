from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    result = []
    visited[start] = True

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result

N = int(input())
M = int(input())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# BFS 탐색 결과 출력
visited_bfs = {i: False for i in range(1, N+1)}
bfs_result = bfs(graph, 1, visited_bfs)
print(len(bfs_result)-1)