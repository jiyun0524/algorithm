# 3. 그리디 - 예제 1 거스름돈

# # 내가 푼 방법
# N = int(input())

# num_500 = int(N/500)
# num_100 = int((N%500)/100)
# num_50 = int(((N%500)%100)/50)
# num_10 = int((((N%500)%100)%50)/10)

# print(num_500 + num_100 + num_50 + num_10)

# 책 코드
N = int(input())
coin = [500, 100, 50, 10]
count = 0

for i in coin :
    count += N // i
    N %= i

print(count)
