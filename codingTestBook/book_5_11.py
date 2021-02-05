# 5. DFS/BFS - 예제 11 미로탈출

N, M = map(int, input().split())

maze = []
for i in range(N) :
    maze.append(list(map(int, input())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

count = 0

for i in range(N) :
    for j in range(M) :
        if maze[i][j] == 0 :
