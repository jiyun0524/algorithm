# 3. 그리디 - 예제 4 1이 될 때까지

N, K = map(int, input().split())
count = 0

while True : # 여러번의 연산이 필요하기 때문에 반복 (반복문)
    if N % K == 0 : # N이 K의 배수이면
        N //= K # N을 K로 계속나눔
        count += 1 # 나눌 때 마다 1회씩 카운트 추가
        print(N, K, count)
        if N == K : # 돌리다가 N이 K랑 같은 수가 되면 나눴을 때 어짜피 1이니까
            count += 1 # 나눈 셈 치고 1 더하기
            break
        else :
            continue
    else :
        N -= 1
        count += 1

print(count)