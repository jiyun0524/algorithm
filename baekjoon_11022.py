x = int(input())

for i in range(x) : 
    A,B = map(int, input().split( ))
    print("Case #%d: %d + %d = %d"%(i+1,A,B,A+B))