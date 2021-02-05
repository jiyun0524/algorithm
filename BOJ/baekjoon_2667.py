N = int(input())

apt = []

for i in range(N) :
    apt.append(list(map(int, input())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

count = 0
test = []
queue = []

for i in range(N) :
    for j in range(N) :
        if apt[i][j] == 0 :
            queue.append((i,j))
            apt[i][j] = 1
            while queue :
                cx, cy = queue.pop(0)
                for k in range(4) :
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    if 0 <= nx < N and 0 <= ny < N :
                        if apt[nx][ny] == 0 :
                            queue.append((nx, ny))
                            apt[nx][ny] = 1
            else :
                count += 1

print(len(test))
for i in sorted(test) :
    print(i)