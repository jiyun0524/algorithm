from collections import deque

while True :
    w, h = map(int, input().split( ))
    if w == 0 and h == 0 :
        break
    
    land = [list(map(int, input().split( ))) for _ in range(h)]

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, -1, 0]

    queue = deque()
    count = 0
    for i in range(h) :
        for j in range(w) :
            if land[i][j] == 1 :
                queue.append((i, j))
                land[i][j] = 2
                while queue :
                    cx, cy = queue.popleft()
                    for k in range(8) :
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        if 0 <= nx < h and 0 <= ny < w :
                            if land[nx][ny] == 1 :
                                queue.append((nx, ny))
                                land[nx][ny] = 2
                count += 1
    print(count)