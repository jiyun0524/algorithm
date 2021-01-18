# 4. 구현 - 예제 1-1 상하좌우

N = int(input())
print(N)
for i in range(N) :
    for j in range(N) :
        print(j, end=' ')
    print(i,j)