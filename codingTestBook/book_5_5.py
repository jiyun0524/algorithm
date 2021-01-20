# 5. DFS/BFS - 예제 5 팩토리얼

def factorial_function(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result

print(factorial_function(5))