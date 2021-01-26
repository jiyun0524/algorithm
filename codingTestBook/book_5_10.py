# 5. DFS/BFS - 예제 10 음료수 얼려 먹기

from collections import deque

M, N = map(int, input().split( ))

ice = []
for i in range(M) :
    ice.append(list(map(int, input())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

queue = deque()
count = 0

for i in range(M) :
    for j in range(N) :
        if ice[i][j] == 0 :
            queue.append((i,j))
            ice[i][j] = 1
            while queue :
                cx, cy = queue.popleft()
                for k in range(4) :
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    if 0 <= nx < M and 0 <= ny < N :
                        if ice[nx][ny] == 0 :
                            queue.append((nx, ny))
                            ice[nx][ny] = 1
            else :
                count += 1
print(count)