from collections import deque
# 상 하 좌 우 좌상 우상 좌하 우하
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,1,-1,-1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))


while True:
    w, h = map(int,input().split())
    graph = []
    count = 0
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)
    
