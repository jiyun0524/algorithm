# 5. DFS/BFS - 예제 8 DFS 예제

def dfs(graph, v, visited) :
    visited[v] = True # 첫 출발 노드는 항상 먼저 방문하는거니까
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, v, visited)

graph = [
            [],
            [2,3,8],
            [1,7],
            [1,4,5],
            [3,5],
            [3,4],
            [7],
            [2,6,8],
            [1,7]
        ]

visited = [False] * 9

dfs(graph, 1, visited)