# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y) # 좌
        dfs(x,y-1) # 상
        dfs(x+1,y) # 우
        dfs(x,y+1) # 하
        return True
    else:
        return False

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)