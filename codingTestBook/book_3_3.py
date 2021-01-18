# 3. 그리디 - 예제 3 숫자 카드 게임

# 내가 푼 방법
M, N = map(int, input().split( ))
arr = []
min_num = []

for i in range(M) :
    arr.append(list(map(int, input().split())))
    min_num.append(min(arr[i]))

min_num.sort()
print(min_num[-1])

# 책에 해설 이해안됨 ㅇㅅㅇ