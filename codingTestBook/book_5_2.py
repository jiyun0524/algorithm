# 5. DFS/BFS - 예제 2 큐

# 5 2 3 7 del 1 4 del

from collections import deque
# 큐 구현을 위해 deque 라이브러리를 사용함
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# queue.pop() 
# queue는 선입선출이기 때문에 맨 앞 자리 수를 제거해야하므로 이거 안됨
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)