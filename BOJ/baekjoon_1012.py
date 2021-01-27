T = int(input())
M, N, K = map(int, input().split())

X, Y = [[0] * (K+1) for _ in range(K+1)]

for _ in range(K) :
    X, Y = map(int, input().split())

print(T, M, N, K, X, Y)