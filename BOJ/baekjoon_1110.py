first = str(input()) # 기존 첫번째 값
middle = 0 # n번째 값
cycle = 0 # 몇 번 돌아야 같은 값이 나오는지
last = 0

first = str(first)

while middle < 100 :
    for i in range(True) :
        middle += int(first[i])

        if (middle<10) :
            next = str(middle)
            next = next.zfill(2)

        last = first[-1] + next[-1]
        print(middle, last)

        if (last == first) :
            break
            print(cycle)
        else :
            cycle += 1
            continue


# for i in range(True) :
#     middle += int(first[i])
#     print(middle)

#     if (middle<10) :
#         next = str(middle)
#         next = next.zfill(2)

#     last = first[-1] + next[-1]
#     print(middle, last)
#     cycle += 1

#     if (last == first) :
#         break
#         print(cycle)