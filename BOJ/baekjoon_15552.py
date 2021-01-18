import sys

x = int(input())

for i in range(x) :
    A,B = map(int, sys.stdin.readline().split( ))
    print(A+B)