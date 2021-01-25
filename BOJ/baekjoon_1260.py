from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

visited = [False] * (N+1)

for _ in range(M) : 
    x, y = map(int,input().split())
    graph[x][y], graph[y][x] = 1, 1

def dfs(v) :
    visited[v] = True # 첫 출발 노드는 항상 먼저 방문하는거니까
    print(v, end=' ')
    for i in range(1, N+1) :
        if not visited[i] and graph[v][i] == 1 :
            dfs(i)

def bfs(v) :
    queue = deque([v])
    visited[v] = False # dfs를 실행하고나면 방문처리가 돼 있기 때문에 False로.
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N+1) :
            if visited[i] and graph[v][i] == 1 :
                queue.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)

# N, M, V = map(int, input().split())
# graph = [[0]*(N+1) for _ in range(N+1)] 
# visited = [False] * (N+1) 

# for _ in range(M): 
#     a, b = map(int, input().split()) 
#     graph[a][b] = 1 
#     graph[b][a] = 1 

# def dfs(v): 
#     visited[v] = True 
#     print(v, end=' ') 
#     for i in range(1, N + 1): 
#         if not visited[i] and graph[v][i] == 1: 
#             dfs(i) 

# def bfs(v): 
#     queue = [v] 
#     visited[v] = False # dfs 실행 시에 True로 방문처리 되어있기 때문에, 여기선 False로 방문처리 
#     while queue: 
#         v = queue.pop(0) 
#         print(v, end=' ') 
#         for i in range(1, N+1): 
#             if visited[i] and graph[v][i] == 1: 
#                 queue.append(i) 
#                 visited[i] = False 

# dfs(V) 
# print() 
# bfs(V)
