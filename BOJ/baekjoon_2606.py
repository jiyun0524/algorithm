N = int(input())
M = int(input())

virus = [[0] * (N + 1) for _ in range(N+1)]
queue = []

for _ in range(M) :
    x, y = map(int,input().split())
    virus[x][y], virus[y][x] = 1, 1


def dfs(start) :
    queue.append(start)
    for i in range(1, N+1) :
        if (i not in queue) and (virus[start][i] == 1) :
            dfs(i)
    return (len(queue) - 1)

print(dfs(1))