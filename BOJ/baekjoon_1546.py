N = int(input())
score = list(map(int, input().split( )))
M = max(score)

for i in range(N) :
    score[i] = score[i]/M*100
avg = sum(score)/N
print(avg)