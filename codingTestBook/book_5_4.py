# 5. DFS/BFS - 예제 4 재귀함수의 종료조건

def recursive_function(i) :
    if i == 100 :
        return
    print(i, '번째 숫자가 ', i+1, '번째 숫자를 호출합니다')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다')

recursive_function(1)
