# 4. 구현 - 예제 1-2 시각

N = int(input())
count = 0

for i in range(0, B) :
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) + str(j) +str(k) :
                count += 1
print(count)