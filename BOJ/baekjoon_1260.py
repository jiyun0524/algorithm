from collections import deque

N, M, V = map(int, input().split())

graph = []
graph.append([])
for i in range(M) : 
    graph.append(list(map(int, input().split())))

def dfs(graph, startDFS, visitedDFS) :
    visitedDFS[startDFS] = True # 첫 출발 노드는 항상 먼저 방문하는거니까
    print(startDFS, end=' ')
    for i in graph[startDFS] :
        if not visitedDFS[i] :
            dfs(graph, i, visitedDFS)

def bfs(graph, startBFS, visitedBFS) :
    queue = deque([startBFS])
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