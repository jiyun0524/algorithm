def selfNum(n) :
    arr = 0
    for i in list(str(n)) :
        arr = arr + int(i)
    return int(n) + arr

arr = []

for i in range(10001) :
    x = selfNum(i)
    arr.append(x)

for j in range(10001) :
    if j in arr:
        pass
    else :
        print(j)