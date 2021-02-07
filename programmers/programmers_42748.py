def solution(array, commands):
    answer = []
    newArr = []
    for x,y,z in commands :
        newArr = array[x-1:y]
        newArr.sort()
        answer.append(newArr[z-1])
    return answer