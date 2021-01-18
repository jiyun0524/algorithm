N = int(input())

for i in range(N) :
    num = str(input())
    count = 0
    total = 0

    for j in range(len(num)) :

        if num[j] == "O" :
            count += 1
            total += count

        elif num[j] == "X":
            count = 0 #더하기가 0으로 리셋돼야함. +=였다면 OOXO일때 마지막 O에서 원래 1이 더해져야하는데 3이더해짐
            total += 0
    print(total)