array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

for x,y,z in commands :
    answer = []
    newArr = array[x-1:y]
    newArr.sort()
    answer.append(newArr[z-1])
    print(answer)