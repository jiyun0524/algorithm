# 5. DFS/BFS - 예제 1 스택
# 5 2 3 7 DEL 1 4 DEL

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) # 순서 거꾸로 출력