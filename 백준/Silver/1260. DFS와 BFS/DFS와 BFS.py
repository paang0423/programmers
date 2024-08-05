from collections import deque

def dfs(graph, start, visited):
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            # 인접 노드를 역순으로 정렬해서 스택에 추가
            for neighbor in sorted(graph[node], reverse=True):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return result

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

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 탐색 결과 출력
visited_dfs = {i: False for i in range(1, N+1)}
dfs_result = dfs(graph, V, visited_dfs)
print(" ".join(map(str, dfs_result)))

# BFS 탐색 결과 출력
visited_bfs = {i: False for i in range(1, N+1)}
bfs_result = bfs(graph, V, visited_bfs)
print(" ".join(map(str, bfs_result)))
