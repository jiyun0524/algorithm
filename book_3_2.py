# 큰 수의 법칙

# 내가 푼 방법 (예시 2와 동일한 답)
N,M,K = map(int, input().split( ))
num = list(map(int, input().split( )))
num.sort()

max_num = num[-1] # 가장 큰 수
next_num = num[-2] # 그 다음 큰 수

cycle = int(M/K)
largeCount = K
nextCount = int(M%K)

print(((max_num * largeCount) * cycle + (next_num * nextCount)))

# # 책 코드 (뭔소린지모르겍노 ㅇㅅㅇㅋ)
# N, M, K = map(int, input().split( ))
# data = list(map(int, input().split( )))

# data.sort()
# first = data[N-1]
# second = data[N-2]

# result = 0
# while True : 
#     for i in range(K) :
#         if M == 0 :
#             break
#         result += first
#         M -= 1
#     if M == 0 :
#         break
#     result += second
#     M -= 1
# print(result)