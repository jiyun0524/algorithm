from collections import deque

N, M, V = map(int, input().split())

graph = []
graph.append([])
for i in range(M) : 
    graph.append(list(map(int, input().split())))

def dfs(graph, V, visited) :
    visited[V] = True # 첫 출발 노드는 항상 먼저 방문하는거니까
    print(V, end=' ')
    for i in graph[V] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, V, visited) :
    queue = deque([V])
    visited[V] = True
    while queue :
        newV = queue.popleft()
        print(newV, end=' ')
        for i in graph[newV] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

visited = [False] * M

dfs(graph, V, visited)

bfs(graph, V, visited)