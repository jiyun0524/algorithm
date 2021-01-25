from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N+1)]
queue = []

for _ in range(M) : 
    x, y = map(int,input().split())
    queue[x][y], queue[y][x] = 1, 1

def dfs(graph, startDFS, visitedDFS) :
    visitedDFS[startDFS] = True # 첫 출발 노드는 항상 먼저 방문하는거니까
    print(startDFS, end=' ')
    for i in graph[startDFS] :
        if not visitedDFS[i] :
            dfs(graph, i, visitedDFS)

def bfs(graph, startBFS, visitedBFS) :
    visitedBFS[startBFS] = True
    while queue :
        popBFS = queue.popleft()
        print(popBFS, end=' ')
        for i in graph[popBFS] :
            if not visitedBFS[i] :
                queue.append(i)
                visitedBFS[i] = True

visitedDFS = [False] * M
visitedBFS = [False] * M

dfs(graph, V, visitedDFS)
print()
bfs(graph, V, visitedBFS)