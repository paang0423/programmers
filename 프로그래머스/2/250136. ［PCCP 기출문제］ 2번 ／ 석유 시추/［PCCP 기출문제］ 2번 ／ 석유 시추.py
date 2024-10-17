from collections import deque

def bfs(start_x, start_y, graph, visited):
    amount = 1
    axis = [(start_x, start_y)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    amount += 1
                    queue.append((nx, ny))
                    axis.append((nx, ny))
    
    return axis, amount

def solution(land):
    answer = 0
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    col_oil = [0] * len(land[0])  # 각 열에 대한 석유량 저장

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and not visited[i][j]:
                # BFS로 덩어리를 탐색하고, 해당 덩어리에 속한 좌표와 석유량을 얻음
                axis, amount = bfs(i, j, land, visited)
                
                # 이 덩어리가 속하는 열마다 석유량을 더함, 같은 열에서 덩어리는 한 번만 더함
                columns_processed = set()  # 중복된 열 처리 방지
                for x, y in axis:
                    if y not in columns_processed:  # 같은 열에서 덩어리 중복 계산 방지
                        col_oil[y] += amount
                        columns_processed.add(y)  # 해당 열을 처리했음을 기록

    # 가장 많은 석유량을 찾음
    answer = max(col_oil)
    
    return answer

# 테스트
print(solution([[1, 0, 1, 0, 1, 1], 
                [1, 0, 1, 0, 0, 0], 
                [1, 0, 1, 0, 0, 1], 
                [1, 0, 0, 1, 0, 0], 
                [1, 0, 0, 1, 0, 1], 
                [1, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 1]]))
